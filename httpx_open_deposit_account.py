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

user_id = create_user_response_data["user"]["id"]
create_deposit_account_url = f"{base_url}/accounts/open-deposit-account"
create_deposit_account_payload = {"userId": user_id}

create_deposit_account_response = httpx.post(
    url=create_deposit_account_url, json=create_deposit_account_payload
)
create_deposit_account_status_code = create_deposit_account_response.status_code
create_deposit_account_response_data = create_deposit_account_response.json()
print(f"Status code: {create_deposit_account_status_code}")
print(f"Create deposit account response: {create_deposit_account_response_data}")
