import httpx
from locust import between, task, User

from clients.http.gateway.accounts.client import (
    AccountsGatewayHTTPClient,
    build_accounts_gateway_locust_http_client,
)
from clients.http.gateway.users.client import (
    UsersGatewayHTTPClient,
    build_users_gateway_locust_http_client,
)
from pydantic_create_user import CreateUserResponseSchema


class OpenDebitCardAccountScenarioUser(User):
    host = "localhost"
    wait_time = between(1, 3)
    users_gateway_client: UsersGatewayHTTPClient
    accounts_gateway_client: AccountsGatewayHTTPClient
    create_user_response: CreateUserResponseSchema

    def on_start(self) -> None:
        self.users_gateway_client = build_users_gateway_locust_http_client(
            self.environment
        )
        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_debit_card_account(self) -> None:
        self.accounts_gateway_client = build_accounts_gateway_locust_http_client(
            self.environment
        )
        try:
            self.accounts_gateway_client.open_debit_card_account(
                self.create_user_response.user.id
            )
        except httpx.RequestError:
            pass
