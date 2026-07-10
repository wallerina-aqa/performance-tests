import httpx
from faker import Faker

base_url = "http://localhost:8003"

client = httpx.Client(base_url=base_url)

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

create_user_url = "/api/v1/users"
create_user_response = client.post(url=create_user_url, json=create_user_payload)

create_user_status_code = create_user_response.status_code
create_user_response_data = create_user_response.json()
print(f"Status code: {create_user_status_code}")
print(f"Create user response: {create_user_response_data}")
