import httpx
from faker import Faker

base_url = "http://localhost:8003/api/v1"

faker = Faker()
user_email = faker.email()
user_last_name = faker.last_name()
user_first_name = faker.first_name()
user_middle_name = faker.first_name()
user_phone_number = faker.phone_number()

create_user_payload = {
    "email": user_email,
    "lastName": user_last_name,
    "firstName": user_first_name,
    "middleName": user_middle_name,
    "phoneNumber": user_phone_number,
}

create_user_url = f"{base_url}/users"
create_user_response = httpx.post(url=create_user_url, json=create_user_payload)

create_user_status_code = create_user_response.status_code
create_user_response_data = create_user_response.json()
print(f"Status code: {create_user_status_code}")
print(f"Create user response: {create_user_response_data}")

open_credit_card_url = f"{base_url}/accounts/open-credit-card-account"
user_id = create_user_response_data["user"]["id"]
open_credit_card_payload = {"userId": user_id}

open_credit_card_account_response = httpx.post(
    url=open_credit_card_url, json=open_credit_card_payload
)
open_credit_card_account_status_code = open_credit_card_account_response.status_code
open_credit_card_account_response_data = open_credit_card_account_response.json()
print(f"Status code: {open_credit_card_account_status_code}")
print(f"Open credit card account response: {open_credit_card_account_response_data}")

account_id = open_credit_card_account_response_data["account"]["id"]
get_tariff_document_view_url = f"{base_url}/documents/tariff-document/{account_id}"

get_tariff_document_view_response = httpx.get(url=get_tariff_document_view_url)
get_tariff_document_view_status_code = get_tariff_document_view_response.status_code
get_tariff_document_view_response_data = get_tariff_document_view_response.json()
print(f"Status code: {get_tariff_document_view_status_code}")
print(f"Get tariff document view response: {get_tariff_document_view_response_data}")

get_contract_document_view_url = f"{base_url}/documents/contract-document/{account_id}"

get_contract_document_view_response = httpx.get(url=get_contract_document_view_url)
get_contract_document_view_status_code = get_contract_document_view_response.status_code
get_contract_document_view_response_data = get_contract_document_view_response.json()
print(f"Status code: {get_contract_document_view_status_code}")
print(
    f"Get contract document view response: {get_contract_document_view_response_data}"
)
