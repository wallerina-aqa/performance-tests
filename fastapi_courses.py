import uvicorn
from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel, RootModel
from starlette import status

app = FastAPI()

courses_router = APIRouter(prefix="/api/v1/courses", tags=["courses-service"])


class CourseIn(BaseModel):
    """
    Represents the input data required to create or update a course.

    This model is used for validating data received from API clients.
    The course identifier is intentionally excluded because it is generated
    automatically by the in-memory storage when a new course is created.

    Attributes:
        title: The title of the course.
        max_score: The maximum score that can be achieved for the course.
        min_score: The minimum score required to successfully pass the course.
        description: A short description of the course and its content.
    """

    title: str
    max_score: int
    min_score: int
    description: str


class CourseOut(CourseIn):
    """
    Represents the course data returned by the API.

    This model extends CourseIn with an automatically generated unique
    identifier. It is used as the response model for endpoints that return
    information about one or more courses.

    Attributes:
        id: The unique identifier assigned to the course by the in-memory store.
        title: The title of the course.
        max_score: The maximum score that can be achieved for the course.
        min_score: The minimum score required to successfully pass the course.
        description: A short description of the course and its content.
    """

    id: int


class CoursesStore(RootModel):
    """
    Provides an in-memory storage layer for course entities.

    The store keeps all course data in a Python list and provides basic CRUD
    operations for searching, creating, updating, and deleting courses.

    The storage exists only in application memory and therefore does not
    persist data between application restarts.

    Attributes:
        root: A list containing all CourseOut instances currently stored
        by the application.
    """

    root: list[CourseOut]

    def find(self, course_id: int) -> CourseOut | None:
        """
        Find a course by its unique identifier.

        The method iterates through the in-memory collection and returns the first
        course whose ID matches the provided value.

        Args:
            course_id: The unique identifier of the course to search for.

        Returns:
            The matching CourseOut instance if a course with the specified ID
            exists; otherwise, None.
        """
        return next(filter(lambda course: course.id == course_id, self.root), None)

    def create(self, course_in: CourseIn) -> CourseOut:
        """
        Create and store a new course.

        A new unique identifier is generated inside the storage layer. The input
        model is converted into a CourseOut instance, appended to the in-memory
        collection, and returned to the caller.

        Args:
            course_in: Validated input data describing the course to create.

        Returns:
            The newly created CourseOut instance including its generated ID.
        """
        course = CourseOut(id=len(self.root) + 1, **course_in.model_dump())
        self.root.append(course)
        return course

    def update(self, course_id: int, course_in: CourseIn) -> CourseOut:
        """
        Replace the data of an existing course.

        The method locates the course with the specified identifier, creates a new
        CourseOut instance using the supplied input data while preserving the
        original course ID, and replaces the existing item in the in-memory list.

        The caller is expected to ensure that the course exists before invoking
        this method.

        Args:
            course_id: The unique identifier of the course to update.
            course_in: Validated course data that will replace the existing data.

        Returns:
            The updated CourseOut instance.

        Raises:
            StopIteration: If no course with the specified identifier exists.
        """
        idx = next(
            idx for idx, course in enumerate(self.root) if course.id == course_id
        )
        updated = CourseOut(id=course_id, **course_in.model_dump())
        self.root[idx] = updated
        return updated

    def delete(self, course_id: int) -> None:
        """
        Delete a course from the in-memory storage.

        The method rebuilds the internal list while excluding the course whose
        identifier matches the provided value. If no matching course exists,
        the contents of the store remain unchanged.

        Args:
            course_id: The unique identifier of the course to remove.

        Returns:
            None.
        """
        self.root = [course for course in self.root if course.id != course_id]


store = CoursesStore(root=[])


@courses_router.get("/{course_id}", response_model=CourseOut)
async def get_course(course_id: int):
    """
    Retrieve a single course by its unique identifier.

    Endpoint:
        GET /api/v1/courses/{course_id}

    The endpoint searches the in-memory store for a course with the specified
    ID. If the course exists, its complete data is returned using the
    CourseOut response model.

    Args:
        course_id: The unique identifier of the requested course.

    Returns:
        The CourseOut instance corresponding to the requested course.

    Raises:
        HTTPException: HTTP 404 Not Found if no course with the specified
        identifier exists.
    """
    if not (course := store.find(course_id)):
        raise HTTPException(
            detail=f"Course with id {course_id} not found",
            status_code=status.HTTP_404_NOT_FOUND,
        )

    return course


@courses_router.get("", response_model=list[CourseOut])
async def get_courses():
    """
    Retrieve all courses currently stored in memory.

    Endpoint:
        GET /api/v1/courses

    The endpoint returns the complete collection of courses available in the
    in-memory store. If no courses have been created yet, an empty list is
    returned.

    Returns:
        A list of CourseOut instances representing all stored courses.
    """
    return store.root


@courses_router.post("", response_model=CourseOut, status_code=status.HTTP_201_CREATED)
async def create_course(course: CourseIn):
    """
    Create a new course.

    Endpoint:
        POST /api/v1/courses

    The request body is validated against the CourseIn model. The validated
    data is then passed to the in-memory store, where a unique identifier is
    generated and a new CourseOut instance is created.

    Args:
        course: Validated course data received in the request body.

    Returns:
        The newly created CourseOut instance including its generated ID.

    HTTP Status:
        201 Created on successful course creation.
    """
    return store.create(course)


@courses_router.put("/{course_id}", response_model=CourseOut)
async def update_course(course_id: int, course: CourseIn):
    """
    Update an existing course by its unique identifier.

    Endpoint:
        PUT /api/v1/courses/{course_id}

    The endpoint first verifies that a course with the specified identifier
    exists. If found, the existing course data is replaced with the validated
    data received in the request body while preserving the original ID.

    Args:
        course_id: The unique identifier of the course to update.
        course: Validated course data received in the request body.

    Returns:
        The updated CourseOut instance.

    Raises:
        HTTPException: HTTP 404 Not Found if no course with the specified
        identifier exists.
    """
    if not store.find(course_id):
        raise HTTPException(
            detail=f"Course with id {course_id} not found",
            status_code=status.HTTP_404_NOT_FOUND,
        )

    return store.update(course_id, course)


@courses_router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_id: int):
    """
    Delete an existing course by its unique identifier.

    Endpoint:
        DELETE /api/v1/courses/{course_id}

    The endpoint verifies that the requested course exists before removing it
    from the in-memory storage. If no course with the provided identifier can
    be found, the request is rejected with an HTTP 404 response.

    Args:
        course_id: The unique identifier of the course to delete.

    Returns:
        None. A successful deletion produces an empty response body.

    Raises:
        HTTPException: HTTP 404 Not Found if no course with the specified
        identifier exists.

    HTTP Status:
        204 No Content when the course is successfully deleted.
    """
    if not store.find(course_id):
        raise HTTPException(
            detail=f"Course with id {course_id} not found",
            status_code=status.HTTP_404_NOT_FOUND,
        )

    store.delete(course_id)


app.include_router(courses_router)

if __name__ == "__main__":
    uvicorn.run("fastapi_courses:app", reload=True)
