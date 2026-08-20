from locust import task

from clients.http.gateway.accounts.schema import (
    OpenDebitCardAccountResponseSchema,
)
from clients.http.gateway.locust import GatewayHttpSequentialTaskSet
from clients.http.gateway.users.schema import CreateUserResponseSchema
from tools.locust.user import LocustBaseUser


class IssuePhysicalCardSequentialTaskSet(GatewayHttpSequentialTaskSet):
    create_user_response: CreateUserResponseSchema | None = None
    user_id: str | None = None

    open_debit_card_account_response: OpenDebitCardAccountResponseSchema | None = None
    account_id: str | None = None

    @task
    def create_user(self):
        self.create_user_response = self.users_gateway_client.create_user()

        if not self.create_user_response:
            return

        self.user_id = self.create_user_response.user.id

    @task
    def open_debit_card_account(self):
        if self.user_id is None:
            return

        self.open_debit_card_account_response = (
            self.accounts_gateway_client.open_debit_card_account(user_id=self.user_id)
        )

        if not self.open_debit_card_account_response:
            return

        self.account_id = self.open_debit_card_account_response.account.id

    @task
    def issue_physical_card(self):
        if self.user_id is None or self.account_id is None:
            return

        self.cards_gateway_client.issue_physical_card(
            user_id=self.user_id, account_id=self.account_id
        )


class IssuePhysicalCardUser(LocustBaseUser):
    tasks = [IssuePhysicalCardSequentialTaskSet]
