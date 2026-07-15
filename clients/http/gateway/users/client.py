from faker import Faker
from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.users.schema import (
    GetUserResponseSchema,
    CreateUserResponseSchema,
    CreateUserRequestSchema,
)


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

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Создание нового пользователя.

        :param request: Словарь с данными нового пользователя.
        :return: Ответ от сервера (объект httpx.Response).
        """

        return self.post(f"api/v1/users", json=request.model_dump(by_alias=True))

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

    def create_user(self) -> CreateUserResponseSchema:
        faker = Faker()
        user_email = faker.email()
        user_last_name = faker.last_name()
        user_first_name = faker.first_name()
        user_middle_name = faker.first_name()
        user_phone_number = faker.phone_number()

        create_user_request = CreateUserRequestSchema(
            email=user_email,
            last_name=user_last_name,
            first_name=user_first_name,
            middle_name=user_middle_name,
            phone_number=user_phone_number,
        )
        response = self.create_user_api(create_user_request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def build_users_http_client() -> UsersGatewayHTTPClient:
    """
    Функция создаёт экземпляр UsersGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию UsersGatewayHTTPClient.
    """
    return UsersGatewayHTTPClient(client=build_gateway_http_client())
