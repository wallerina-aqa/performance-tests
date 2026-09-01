from locust import task, events
from locust.env import Environment

from clients.grpc.gateway.locust import GatewayGRPCTaskSet
from seeds.scenarios.existing_user_get_operations import (
    ExistingUserGetOperationsSeedsScenario,
)
from seeds.schema.result import SeedUserResult
from tools.locust.user import LocustBaseUser


@events.init.add_listener
def init(environment: Environment, **kwargs):
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()
    environment.seeds = seeds_scenario.load()


class GetOperationsTaskSet(GatewayGRPCTaskSet):
    seed_user: SeedUserResult
    user_id: str
    account_id: str

    def on_start(self) -> None:
        super().on_start()
        self.seed_user = self.user.environment.seeds.get_random_user()
        self.user_id = self.seed_user.user_id
        self.account_id = self.seed_user.credit_card_accounts[0].account_id

    @task
    def get_accounts(self):
        self.accounts_gateway_client.get_accounts(user_id=self.user_id)

    @task(4)
    def get_operations(self):
        self.operations_gateway_client.get_operations(account_id=self.account_id)

    @task(2)
    def get_operations_summary(self):
        self.operations_gateway_client.get_operations_summary(
            account_id=self.account_id
        )


class GetOperationsScenarioUser(LocustBaseUser):
    tasks = [GetOperationsTaskSet]
