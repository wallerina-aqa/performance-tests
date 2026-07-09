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

open_debit_card_account_url = f"{base_url}/accounts/open-debit-card-account"
user_id = create_user_response_data["user"]["id"]
open_debit_card_account_payload = {
    "userId": user_id,
}

open_debit_card_account_response = httpx.post(
    url=open_debit_card_account_url, json=open_debit_card_account_payload
)
open_debit_card_account_status_code = open_debit_card_account_response.status_code
open_debit_card_account_response_data = open_debit_card_account_response.json()
print(f"Status code: {open_debit_card_account_status_code}")
print(f"Open debit card account response: {open_debit_card_account_response_data}")

issue_virtual_card_url = f"{base_url}/cards/issue-virtual-card"
account_id = open_debit_card_account_response_data["account"]["id"]
issue_virtual_card_payload = {
    "userId": user_id,
    "accountId": account_id,
}

issue_virtual_card_response = httpx.post(
    url=issue_virtual_card_url, json=issue_virtual_card_payload
)
issue_virtual_card_status_code = issue_virtual_card_response.status_code
issue_virtual_card_response_data = issue_virtual_card_response.json()
print(f"Status code: {issue_virtual_card_status_code}")
print(f"Issue virtual card response: {issue_virtual_card_response_data}")
