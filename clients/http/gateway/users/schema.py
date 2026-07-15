from pydantic import BaseModel, EmailStr, Field, ConfigDict
from pydantic.alias_generators import to_camel


class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """

    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class GetUserResponseSchema(BaseModel):
    """
    Описание структуры ответа получения пользователя.
    """

    user: UserSchema


class CreateUserRequestSchema(BaseModel):
    """
    Структура данных для создания нового пользователя.
    """

    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )

    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str
    phone_number: str


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """

    user: UserSchema
