from pydantic import BaseModel


class Address(BaseModel):
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address
    is_active: bool = False


user = User(
    id=4444,
    name="Alice",
    email="alice@example.com",
    is_active=True,
    address=Address(city="New York", zip_code="5555"),
)
print(user)
