import httpx
from faker import Faker

faker = Faker()

base_url = "http://localhost:8003/api/v1"

# Создаем пользователя
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

# Создаем кредитный счет
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

# Совершаем операцию покупки
make_purchase_operation_url = f"{base_url}/operations/make-purchase-operation"
card_id = open_credit_card_account_response_data["account"]["cards"][0]["id"]
account_id = open_credit_card_account_response_data["account"]["id"]
make_purchase_operation_payload = {
    "status": "IN_PROGRESS",
    "amount": 77.99,
    "cardId": card_id,
    "accountId": account_id,
    "category": "taxi",
}

make_purchase_operation_response = httpx.post(
    url=make_purchase_operation_url, json=make_purchase_operation_payload
)
make_purchase_operation_status_code = make_purchase_operation_response.status_code
make_purchase_operation_response_data = make_purchase_operation_response.json()
print(f"Status code: {make_purchase_operation_status_code}")
print(f"Make top up operation response: {make_purchase_operation_response_data}")

# Получаем чек по операции
operation_id = make_purchase_operation_response_data["operation"]["id"]
get_operation_receipt_url = f"{base_url}/operations/operation-receipt/{operation_id}"

get_operation_receipt_response = httpx.get(url=get_operation_receipt_url)
get_operation_receipt_status_code = get_operation_receipt_response.status_code
get_operation_receipt_response_data = get_operation_receipt_response.json()
print(f"Status code: {get_operation_receipt_status_code}")
print(f"Get operation receipt response: {get_operation_receipt_response_data}")

# Мне очень жаль, что ваш аккаунт на Хабре забанили.
# Если бы у меня было такое количество таких объемных статей и их просто удалили,
# я бы недели 1,5 просто рыдала под музыку Radiohead.
# А вы сделали свой сайт и занимаетесь бесплатным курсом по API (на сайте видно).
# Вы - молодец! И наверное кость в горле у всех школ по автоматизации тестирования :)
