from clients.http.gateway.accounts.client import build_accounts_http_client
from clients.http.gateway.cards.client import build_cards_http_client
from clients.http.gateway.users.client import build_users_http_client

users_gateway_client = build_users_http_client()
cards_gateway_client = build_cards_http_client()
accounts_gateway_client = build_accounts_http_client()

create_user_response = users_gateway_client.create_user()
print(
    f"Create user response: "
    f"{create_user_response.model_dump_json(indent=2, by_alias=True)}"
)

user_id = create_user_response.user.id
open_debit_card_account_response = accounts_gateway_client.open_debit_card_account(
    user_id=user_id
)
print(
    f"Open debit card account response: "
    f"{open_debit_card_account_response.model_dump_json(indent=2, by_alias=True)}"
)

account_id = open_debit_card_account_response.account.id
issue_physical_card_response = cards_gateway_client.issue_physical_card(
    user_id=user_id, account_id=account_id
)
print(
    f"Issue physical card response: "
    f"{issue_physical_card_response.model_dump_json(indent=2, by_alias=True)}"
)
