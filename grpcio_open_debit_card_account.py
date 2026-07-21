import grpc

from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import (
    AccountsGatewayServiceStub,
)
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import (
    OpenDebitCardAccountRequest,
)
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import (
    UsersGatewayServiceStub,
)
from tools.fakers import fake

channel = grpc.insecure_channel("localhost:9003")

users_gateway_service = UsersGatewayServiceStub(channel)
create_user_request = CreateUserRequest(
    email=fake.email(),
    last_name=fake.last_name(),
    first_name=fake.first_name(),
    middle_name=fake.last_name(),
    phone_number=fake.phone_number(),
)
create_user_response = users_gateway_service.CreateUser(create_user_request)
print("Create user response:", create_user_response)

accounts_gateway_service = AccountsGatewayServiceStub(channel)
user_id = create_user_response.user.id
open_debit_card_account_request = OpenDebitCardAccountRequest(user_id=user_id)
open_debit_card_account_response = accounts_gateway_service.OpenDebitCardAccount(
    open_debit_card_account_request
)
print("Open debit card account response:", open_debit_card_account_response)
