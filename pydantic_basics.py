from datetime import date
from faker import Faker
from pydantic import BaseModel, Field, ConfigDict, HttpUrl, EmailStr, ValidationError
from pydantic.alias_generators import to_camel

faker = Faker()


class DocumentSchema(BaseModel):
    url: HttpUrl
    document: str


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


try:
    tariff = DocumentSchema(url="localhost", document="tariff")
except ValidationError as error:
    print(error)
    print(error.errors())

print(
    UserSchema(
        id="user-id",
        email="email@gmail.com",
        lastName="last_name",
        firstName="first_name",
        middleName="middle_name",
        phoneNumber="phone_number",
    )
)


class CardSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = "card-id"
    pin: str = "1234"
    cvv: str = "123"
    type: str = "PHYSICAL"
    status: str = "ACTIVE"
    account_id: str = Field(alias="accountId", default="account-id")
    card_number: str = Field(alias="cardNumber", default="1234123412341234")
    card_holder: str = Field(alias="cardHolder", default="Alice Smith")
    expiry_date: date = Field(alias="expiryDate", default=date(2026, 7, 11))
    payment_system: str = Field(alias="paymentSystem", default="VISA")


class AccountSchema(BaseModel):
    id: str = Field(default_factory=lambda: faker.uuid4())
    type: str = "CREDIT_CARD"
    cards: list[CardSchema] = Field(default_factory=list)
    status: str = "ACTIVE"
    balance: float = 25000

    def get_account_name(self) -> str:
        return f"{self.status} {self.type}"


account1 = AccountSchema()
account2 = AccountSchema()
print(account1)
print(account2)
print(account1.get_account_name())
print(account2.get_account_name())


account_default_model = AccountSchema(
    id="account-id",
    type="CREDIT_CARD",
    cards=[CardSchema()],
    status="ACTIVE",
    balance=100.57,
)
print("Account default model: ", account_default_model)

account_dict = {
    "id": "account-id",
    "type": "CREDIT_CARD",
    "cards": [
        {
            "id": "card-id",
            "pin": "1234",
            "cvv": "123",
            "type": "PHYSICAL",
            "status": "ACTIVE",
            "accountId": "account-id",
            "cardNumber": "1234123412341234",
            "cardHolder": "Alice Smith",
            "expiryDate": "2026-07-11",
            "paymentSystem": "VISA",
        }
    ],
    "status": "ACTIVE",
    "balance": 777.11,
}

account_dict_model = AccountSchema(**account_dict)
print("Account dict model: ", account_dict_model)
print(account_dict_model.model_dump(by_alias=True))

account_json = """
{
    "id": "account-id",
    "type": "CREDIT_CARD",
    "cards": [
        {
            "id": "card-id",
            "pin": "1234",
            "cvv": "123",
            "type": "PHYSICAL",
            "status": "ACTIVE",
            "accountId": "account-id",
            "cardNumber": "1234123412341234",
            "cardHolder": "Alice Smith",
            "expiryDate": "2026-07-11",
            "paymentSystem": "VISA"
        }
    ],
    "status": "ACTIVE",
    "balance": 777.11
}
"""
account_json_model = AccountSchema.model_validate_json(account_json)
print("Account JSON model: ", account_json_model)
