from locust import task

from clients.grpc.gateway.locust import GatewayGRPCTaskSet
from contracts.services.gateway.accounts.rpc_get_accounts_pb2 import GetAccountsResponse
from contracts.services.gateway.accounts.rpc_open_deposit_account_pb2 import (
    OpenDepositAccountResponse,
)
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse
from tools.locust.user import LocustBaseUser


class GetAccountsTaskSet(GatewayGRPCTaskSet):
    """
    Нагрузочный сценарий, который:
    1. Создаёт нового пользователя.
    2. Открывает депозитный счёт.
    3. Запрашивает список всех счетов для текущего пользователя.

    Использует базовый GatewayGRPCTaskSet и уже созданных в нём GRPC клиентов.
    """

    create_user_response: CreateUserResponse | None = None
    open_deposit_account_response: OpenDepositAccountResponse | None = None
    get_accounts_response: GetAccountsResponse | None = None
    user_id: str | None = None

    @task(2)
    def create_user(self):
        """
        Создаём нового пользователя и сохраняем результат для последующих шагов.
        """

        self.create_user_response = self.users_gateway_client.create_user()
        if self.create_user_response is not None:
            self.user_id = self.create_user_response.user.id

    @task(2)
    def open_deposit_account(self):
        """
        Открываем депозитный счёт для созданного пользователя.
        Проверяем, что предыдущий шаг был успешным.
        """

        if self.user_id is None:
            return

        self.open_deposit_account_response = (
            self.accounts_gateway_client.open_deposit_account(user_id=self.user_id)
        )

    @task(6)
    def get_accounts(self):
        """
        Получаем счета, если счёт был успешно открыт.
        """

        if self.user_id is None:
            return

        self.accounts_gateway_client.get_accounts(user_id=self.user_id)


class GetAccountsUser(LocustBaseUser):
    """
    Пользователь Locust, исполняющий сценарий получения счетов пользователя.
    """

    tasks = [GetAccountsTaskSet]
