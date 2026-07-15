from clients.http.gateway.accounts.client import build_accounts_http_client
from clients.http.gateway.documents.client import build_documents_http_client
from clients.http.gateway.users.client import build_users_http_client

users_gateway_client = build_users_http_client()
accounts_gateway_client = build_accounts_http_client()
documents_gateway_client = build_documents_http_client()

create_user_response = users_gateway_client.create_user()
print(
    "Create user response: ",
    create_user_response.model_dump_json(indent=2, by_alias=True),
)

user_id = create_user_response.user.id
open_credit_card_account_response = accounts_gateway_client.open_credit_card_account(
    user_id=user_id
)
print(
    "Open credit card account response: ",
    open_credit_card_account_response.model_dump_json(indent=2, by_alias=True),
)

account_id = open_credit_card_account_response.account.id
get_tariff_document_response = documents_gateway_client.get_tariff_document(
    account_id=account_id
)
print(
    "Get tariff document response: ",
    get_tariff_document_response.model_dump_json(indent=2),
)

get_contract_document_response = documents_gateway_client.get_contract_document(
    account_id=account_id
)
print(
    "Get contract document response: ",
    get_contract_document_response.model_dump_json(indent=2),
)
