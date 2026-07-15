from enum import StrEnum

from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel


class CardType(StrEnum):
    VIRTUAL = "VIRTUAL"
    PHYSICAL = "PHYSICAL"


class CardStatus(StrEnum):
    ACTIVE = "ACTIVE"
    FROZEN = "FROZEN"
    CLOSED = "CLOSED"


class CardPaymentSystem(StrEnum):
    VISA = "VISA"
    MASTERCARD = "MASTERCARD"


class CardSchema(BaseModel):
    """
    Описание структуры платёжной карты.
    """

    id: str
    pin: str
    cvv: str
    type: CardType
    status: CardStatus
    account_id: str = Field(alias="accountId")
    card_number: str = Field(alias="cardNumber")
    card_holder: str = Field(alias="cardHolder")
    expiry_date: str = Field(alias="expiryDate")
    payment_system: CardPaymentSystem = Field(alias="paymentSystem")


class IssueVirtualCardRequestSchema(BaseModel):
    """
    Структура данных для выпуска виртуальной карты
    """

    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )

    user_id: str
    account_id: str


class IssueVirtualCardResponseSchema(BaseModel):
    """
    Описание структуры ответа выпуска виртуальной карты.
    """

    card: CardSchema


class IssuePhysicalCardRequestSchema(BaseModel):
    """
    Структура данных для выпуска физической карты.
    """

    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )

    user_id: str
    account_id: str


class IssuePhysicalCardResponseSchema(BaseModel):
    """
    Описание структуры ответа выпуска физической карты.
    """

    card: CardSchema
