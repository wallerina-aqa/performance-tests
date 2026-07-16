from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, HttpUrl, Field
from pydantic.alias_generators import to_camel

from tools.fakers import fake


class GetOperationsQuerySchema(BaseModel):
    """
    Структура данных для получения списка операций счета.
    """

    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )

    account_id: str


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationSchema(BaseModel):
    """
    Описание структуры операции
    """

    model_config = ConfigDict(alias_generator=to_camel)

    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str
    category: str
    created_at: datetime
    account_id: str


class GetOperationsResponseSchema(BaseModel):
    """
    Описание структуры ответа получения всех операций счета.
    """

    operations: list[OperationSchema]


class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Структура данных для получения статистики по операциям счета.
    """

    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )
    account_id: str


class OperationsSummarySchema(BaseModel):
    """
    Структура статистики по операциям счета.
    """

    model_config = ConfigDict(alias_generator=to_camel)

    spent_amount: float
    received_amount: float
    cashback_amount: float


class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Описание структуры ответа получения статистики по операциям счета.
    """

    summary: OperationsSummarySchema


class OperationReceiptSchema(BaseModel):
    """Описание структуры чека"""

    url: HttpUrl = Field(min_length=1, max_length=2083)
    document: str


class GetOperationReceiptResponseSchema(BaseModel):
    """
    Операция структуры ответа получения чека по операции.
    """

    receipt: OperationReceiptSchema


class GetOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа получения деталей операции.
    """

    operation: OperationSchema


class MakeFeeOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции комиссии.
    """

    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str
    account_id: str


class MakeFeeOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа по созданию операции комиссии.
    """

    operation: OperationSchema


class MakeTopUpOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции пополнения.
    """

    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str
    account_id: str


class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа по созданию операции пополнения.
    """

    operation: OperationSchema


class MakeCashbackOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции кэшбэка.
    """

    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str
    account_id: str


class MakeCashbackOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа по созданию операции кэшбэка.
    """

    operation: OperationSchema


class MakeTransferOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции перевода.
    """

    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str
    account_id: str


class MakeTransferOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа по созданию операции перевода.
    """

    operation: OperationSchema


class MakePurchaseOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции покупки.
    """

    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str
    account_id: str
    category: str = Field(default_factory=fake.category)


class MakePurchaseOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа по созданию операции покупки.
    """

    operation: OperationSchema


class MakeBillPaymentOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции оплаты по счету.
    """

    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str
    account_id: str


class MakeBillPaymentOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа по позданию операции оплаты по счету.
    """

    operation: OperationSchema


class MakeCashWithdrawalOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции снятия наличных.
    """

    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str
    account_id: str


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа по созданию операции снятия наличных.
    """

    operation: OperationSchema
