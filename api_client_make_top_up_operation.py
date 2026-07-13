import json

from clients.http.gateway.accounts.client import build_accounts_http_client
from clients.http.gateway.operations.client import build_operations_http_client
from clients.http.gateway.users.client import build_users_http_client

users_gateway_client = build_users_http_client()
accounts_gateway_client = build_accounts_http_client()
operations_gateway_client = build_operations_http_client()

create_user_response = users_gateway_client.create_user()
print(f"Create user response: {json.dumps(create_user_response, indent=2)}")

user_id = create_user_response["user"]["id"]
open_debit_card_account_response = accounts_gateway_client.open_debit_card_account(
    user_id=user_id
)
print(
    f"Open debit card account response: "
    f"{json.dumps(open_debit_card_account_response, indent=2)}"
)

account_id = open_debit_card_account_response["account"]["id"]
card_id = open_debit_card_account_response["account"]["cards"][0]["id"]
make_top_up_operation_response = operations_gateway_client.make_top_up_operation(
    card_id=card_id, account_id=account_id
)
print(
    f"Make top up operation response: "
    f"{json.dumps(make_top_up_operation_response, indent=2)}"
)
