from locust import task

from clients.grpc.gateway.locust import GatewayGRPCSequentialTaskSet
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import (
    OpenDebitCardAccountResponse,
)
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (
    MakeTopUpOperationResponse,
)
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse
from tools.locust.user import LocustBaseUser


class MakeTopUpOperationSequentialTaskSet(GatewayGRPCSequentialTaskSet):
    create_user_response: CreateUserResponse | None = None
    open_debit_card_account_response: OpenDebitCardAccountResponse | None = None
    account_id: str | None = None

    make_top_up_operation_response: MakeTopUpOperationResponse | None = None
    operation_id: str | None = None

    @task
    def create_user(self):
        self.create_user_response = self.users_gateway_client.create_user()

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


class MakeTopUpOperationScenarioUser(LocustBaseUser):
    tasks = [MakeTopUpOperationSequentialTaskSet]
