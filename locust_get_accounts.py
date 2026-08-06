from locust import task, User, between

from clients.http.gateway.accounts.schema import (
    OpenDepositAccountResponseSchema,
    GetAccountsResponseSchema,
)
from clients.http.gateway.locust import GatewayHttpTaskSet
from pydantic_create_user import CreateUserResponseSchema


class GetAccountsTaskSet(GatewayHttpTaskSet):
    """
    Нагрузочный сценарий, который:
    1. Создаёт нового пользователя.
    2. Открывает депозитный счёт.
    3. Запрашивает список всех счетов для текущего пользователя.

    Использует базовый GatewayHTTPTaskSet и уже созданных в нём API клиентов.
    """

    create_user_response: CreateUserResponseSchema | None = None
    open_deposit_account_response: OpenDepositAccountResponseSchema | None = None
    get_accounts_response: GetAccountsResponseSchema | None = None
    user_id: str

    @task(2)
    def create_user(self):
        """
        Создаём нового пользователя и сохраняем результат для последующих шагов.
        """

        self.create_user_response = self.users_gateway_client.create_user()

    @task(2)
    def open_deposit_account(self):
        """
        Открываем депозитный счёт для созданного пользователя.
        Проверяем, что предыдущий шаг был успешным.
        """

        if not self.create_user_response:
            return

        self.user_id = self.create_user_response.user.id
        self.open_deposit_account_response = (
            self.accounts_gateway_client.open_deposit_account(user_id=self.user_id)
        )

    @task(6)
    def get_accounts(self):
        """
        Получаем счета, если счёт был успешно открыт.
        """

        if not self.open_deposit_account_response:
            return

        self.accounts_gateway_client.get_accounts(user_id=self.user_id)


class GetDocumentsUser(User):
    """
    Пользователь Locust, исполняющий сценарий получения счетов пользователя.
    """

    tasks = [GetAccountsTaskSet]
    host = "localhost"
    wait_time = between(1, 3)
