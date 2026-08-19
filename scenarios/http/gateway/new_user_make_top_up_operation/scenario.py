from locust import task

from clients.http.gateway.accounts.schema import OpenDebitCardAccountResponseSchema
from clients.http.gateway.locust import GatewayHttpSequentialTaskSet
from clients.http.gateway.operations.schema import MakeTopUpOperationResponseSchema
from clients.http.gateway.users.schema import CreateUserResponseSchema
from tools.locust.user import LocustBaseUser


class MakeTopUpOperationSequentialTaskSet(GatewayHttpSequentialTaskSet):
    create_user_response: CreateUserResponseSchema | None = None
    open_debit_card_account_response: OpenDebitCardAccountResponseSchema | None = None
    account_id: str | None = None

    make_top_up_operation_response: MakeTopUpOperationResponseSchema | None = None
    operation_id: str | None = None

    @task
    def create_user(self):
        self.users_gateway_client.create_user()

    @task
    def open_debit_card_account(self):
        if not self.create_user_response:
            return

        user_id = self.create_user_response.user.id
        self.open_debit_card_account_response = (
            self.accounts_gateway_client.open_debit_card_account(user_id=user_id)
        )

    @task
    def make_top_up_operation(self):
        if not self.open_debit_card_account_response:
            return

        card_id = self.open_debit_card_account_response.account.cards[0].id
        account_id = self.open_debit_card_account_response.account.id
        self.account_id = account_id

        self.make_top_up_operation_response = (
            self.operations_gateway_client.make_top_up_operation(
                card_id=card_id, account_id=account_id
            )
        )
        if not self.make_top_up_operation_response:
            return

        self.operation_id = self.make_top_up_operation_response.operation.id

    @task
    def get_operations(self):
        if self.account_id is None:
            return

        self.operations_gateway_client.get_operations(account_id=self.account_id)

    @task
    def get_operations_summary(self):
        if self.account_id is None:
            return

        self.operations_gateway_client.get_operations_summary(
            account_id=self.account_id
        )

    @task
    def get_operation(self):
        if self.operation_id is None:
            return

        self.operations_gateway_client.get_operation(operation_id=self.operation_id)

class MakePurchaseOperationScenarioUser(LocustBaseUser):
    tasks = [MakeTopUpOperationSequentialTaskSet]
