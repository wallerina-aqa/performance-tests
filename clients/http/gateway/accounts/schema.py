from enum import StrEnum

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from clients.http.gateway.cards.schema import CardSchema


class AccountType(StrEnum):
    DEBIT_CARD = "DEBIT_CARD"
    CREDIT_CARD = "CREDIT_CARD"
    DEPOSIT = "DEPOSIT"
    SAVINGS = "SAVINGS"


class AccountStatus(StrEnum):
    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"
    PENDING_CLOSURE = "PENDING_CLOSURE"


class AccountSchema(BaseModel):
    """
    Описание структуры банковского счёта.
    """

    id: str
    type: AccountType
    cards: list[CardSchema]
    status: AccountStatus
    balance: float


class GetAccountsQuerySchema(BaseModel):
    """
    Структура данных для получения списка счетов пользователя.
    """

    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )

    user_id: str


class GetAccountsResponseSchema(BaseModel):
    """
    Описание структуры ответа получения списка счетов.
    """

    accounts: list[AccountSchema]


class OpenDepositAccountRequestSchema(BaseModel):
    """
    Структура данных для открытия депозитного счета.
    """

    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )

    user_id: str


class OpenDepositAccountResponseSchema(BaseModel):
    """
    Описание структуры ответа открытия депозитного счета.
    """

    account: AccountSchema


class OpenSavingsAccountRequestSchema(BaseModel):
    """
    Структура данных для открытия сберегательного счета.
    """

    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )

    user_id: str


class OpenSavingsAccountResponseSchema(BaseModel):
    """
    Описание структуры ответа открытия сберегательного счета.
    """

    account: AccountSchema


class OpenDebitCardAccountRequestSchema(BaseModel):
    """
    Структура данных для открытия дебетового счета.
    """

    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )

    user_id: str


class OpenDebitCardAccountResponseSchema(BaseModel):
    """
    Описание структуры ответа открытия дебетового счета.
    """

    account: AccountSchema


class OpenCreditCardAccountRequestSchema(BaseModel):
    """
    Структура данных для открытия кредитного счета.
    """

    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )

    user_id: str


class OpenCreditCardAccountResponseSchema(BaseModel):
    """
    Описание структуры ответа открытия кредитного счета.
    """

    account: AccountSchema
