from pydantic import BaseModel, ConfigDict, EmailStr
from pydantic.alias_generators import to_camel


class BaseSchema(BaseModel):
    """Базовая схема с поддержкой camelCase."""

    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )


class CreateUserRequestSchema(BaseSchema):
    """Схема запроса на создание пользователя."""

    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str
    phone_number: str


class UserSchema(CreateUserRequestSchema):
    """Схема пользователя."""

    id: str


class CreateUserResponseSchema(BaseSchema):
    """Схема ответа на запрос создания пользователя."""

    user: UserSchema
