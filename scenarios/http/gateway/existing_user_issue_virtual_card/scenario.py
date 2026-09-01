from locust import task, events
from locust.env import Environment

from clients.http.gateway.locust import GatewayHttpTaskSet
from seeds.scenarios.existing_user_issue_virtual_card import (
    ExistingUserIssueVirtualCardSeedsScenario,
)
from seeds.schema.result import SeedUserResult
from tools.locust.user import LocustBaseUser


@events.init.add_listener
def init(environment: Environment, **kwargs):
    seeds_scenario = ExistingUserIssueVirtualCardSeedsScenario()
    seeds_scenario.build()
    environment.seeds = seeds_scenario.load()


class IssueVirtualCardTaskSet(GatewayHttpTaskSet):
    seed_user: SeedUserResult
    user_id: str
    account_id: str

    def on_start(self) -> None:
        super().on_start()
        self.seed_user = self.user.environment.seeds.get_random_user()
        self.user_id = self.seed_user.user_id
        self.account_id = self.seed_user.debit_card_accounts[0].account_id

    @task(5)
    def get_accounts(self):
        self.accounts_gateway_client.get_accounts(user_id=self.user_id)

    @task
    def issue_virtual_card(self):
        self.cards_gateway_client.issue_virtual_card(
            user_id=self.user_id, account_id=self.account_id
        )


class IssueVirtualCardScenarioUser(LocustBaseUser):
    tasks = [IssueVirtualCardTaskSet]
