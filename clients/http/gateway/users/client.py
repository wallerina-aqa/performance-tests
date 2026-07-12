from typing import TypedDict

from faker import Faker
from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class UserDict(TypedDict):
    """
    Описание структуры пользователя.
    """

    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class GetUserResponseDict(TypedDict):
    """
    Описание структуры ответа получения пользователя.
    """

    user: UserDict


class CreateUserRequestDict(TypedDict):
    """
    Структура данных для создания нового пользователя.
    """

    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа создания пользователя.
    """

    user: UserDict


class UsersGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/users сервиса http-gateway.
    """

    def get_user_api(self, user_id: str) -> Response:
        """
        Получить данные пользователя по его user_id.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера (объект httpx.Response).
        """

        return self.get(f"api/v1/users/{user_id}")

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Создание нового пользователя.

        :param request: Словарь с данными нового пользователя.
        :return: Ответ от сервера (объект httpx.Response).
        """

        return self.post(f"api/v1/users", json=request)

    def get_user(self, user_id: str) -> GetUserResponseDict:
        response = self.get_user_api(user_id)
        return response.json()

    def create_user(self) -> CreateUserResponseDict:
        faker = Faker()
        user_email = faker.email()
        user_last_name = faker.last_name()
        user_first_name = faker.first_name()
        user_middle_name = faker.first_name()
        user_phone_number = faker.phone_number()

        create_user_request = CreateUserRequestDict(
            email=user_email,
            lastName=user_last_name,
            firstName=user_first_name,
            middleName=user_middle_name,
            phoneNumber=user_phone_number,
        )
        response = self.create_user_api(create_user_request)
        return response.json()


def build_users_http_client() -> UsersGatewayHTTPClient:
    """
    Функция создаёт экземпляр UsersGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию UsersGatewayHTTPClient.
    """
    return UsersGatewayHTTPClient(client=build_gateway_http_client())
