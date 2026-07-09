import httpx
from faker import Faker

faker = Faker()
user_email = faker.email()

create_user_payload = {
    "email": user_email,
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string",
}
response = httpx.post(
    url="http://localhost:8003/api/v1/users", json=create_user_payload
)
print(f"Create user response: {response.json()}")
print(f"Status code: {response.status_code}")

user_id = response.json()["user"]["id"]
get_user_response = httpx.get(f"http://localhost:8003/api/v1/users/{user_id}")
print(f"Get user response: {get_user_response.json()}")
print(f"Status code: {get_user_response.status_code}")
