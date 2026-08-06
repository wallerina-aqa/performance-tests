from locust import TaskSet, SequentialTaskSet

from clients.grpc.gateway.accounts.client import (
    build_accounts_gateway_locust_grpc_client,
    AccountsGatewayGRPCClient,
)
from clients.grpc.gateway.cards.client import (
    build_cards_gateway_locust_grpc_client,
    CardsGatewayGRPCClient,
)
from clients.grpc.gateway.documents.client import (
    build_documents_gateway_locust_grpc_client,
    DocumentsGatewayGRPCClient,
)
from clients.grpc.gateway.operations.client import (
    build_operations_gateway_locust_grpc_client,
    OperationsGatewayGRPCClient,
)
from clients.grpc.gateway.users.client import (
    build_users_gateway_locust_grpc_client,
    UsersGatewayGRPCClient,
)


class GatewayGRPCTaskSet(TaskSet):
    users_gateway_client: UsersGatewayGRPCClient
    accounts_gateway_client: AccountsGatewayGRPCClient
    cards_gateway_client: CardsGatewayGRPCClient
    documents_gateway_client: DocumentsGatewayGRPCClient
    operations_gateway_client: OperationsGatewayGRPCClient

    def on_start(self) -> None:
        environment = self.user.environment

        self.users_gateway_client = build_users_gateway_locust_grpc_client(environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_grpc_client(
            environment
        )
        self.cards_gateway_client = build_cards_gateway_locust_grpc_client(environment)
        self.documents_gateway_client = build_documents_gateway_locust_grpc_client(
            environment
        )
        self.operations_gateway_client = build_operations_gateway_locust_grpc_client(
            environment
        )


class GatewayGRPCSequentialTaskSet(SequentialTaskSet):
    users_gateway_client: UsersGatewayGRPCClient
    accounts_gateway_client: AccountsGatewayGRPCClient
    cards_gateway_client: CardsGatewayGRPCClient
    documents_gateway_client: DocumentsGatewayGRPCClient
    operations_gateway_client: OperationsGatewayGRPCClient

    def on_start(self) -> None:
        environment = self.user.environment

        self.users_gateway_client = build_users_gateway_locust_grpc_client(environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_grpc_client(
            environment
        )
        self.cards_gateway_client = build_cards_gateway_locust_grpc_client(environment)
        self.documents_gateway_client = build_documents_gateway_locust_grpc_client(
            environment
        )
        self.operations_gateway_client = build_operations_gateway_locust_grpc_client(
            environment
        )
