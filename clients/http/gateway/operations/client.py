from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения списка операций счета.
    """

    accountId: str


class OperationDict(TypedDict):
    """
    Описание структуры операции
    """

    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class GetOperationsResponseDict(TypedDict):
    """
    Описание структуры ответа получения всех операций счета.
    """

    operations: list[OperationDict]


class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура данных для получения статистики по операциям счета.
    """

    accountId: str


class OperationsSummaryDict:
    """
    Структура статистики по операциям счета.
    """

    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class GetOperationsSummaryResponseDict(TypedDict):
    """
    Описание структуры ответа получения статистики по операциям счета.
    """

    summary: OperationsSummaryDict


class OperationReceiptDict(TypedDict):
    """Описание структуры чека"""

    url: str
    document: str


class GetOperationReceiptResponseDict(TypedDict):
    """
    Операция структуры ответа получения чека по операции.
    """

    receipt: OperationReceiptDict


class GetOperationResponseDict(TypedDict):
    """
    Описание структуры ответа получения деталей операции.
    """

    operation: OperationDict


class MakeFeeOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции комиссии.
    """

    status: str
    amount: float
    cardId: str
    accountId: str


class MakeFeeOperationResponseDict(TypedDict):
    """
    Описание структуры ответа по созданию операции комиссии.
    """

    operation: OperationDict


class MakeTopUpOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции пополнения.
    """

    status: str
    amount: float
    cardId: str
    accountId: str


class MakeTopUpOperationResponseDict(TypedDict):
    """
    Описание структуры ответа по созданию операции пополнения.
    """

    operation: OperationDict


class MakeCashbackOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции кэшбэка.
    """

    status: str
    amount: float
    cardId: str
    accountId: str


class MakeCashbackOperationResponseDict(TypedDict):
    """
    Описание структуры ответа по созданию операции кэшбэка.
    """

    operation: OperationDict


class MakeTransferOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции перевода.
    """

    status: str
    amount: float
    cardId: str
    accountId: str


class MakeTransferOperationResponseDict(TypedDict):
    """
    Описание структуры ответа по созданию операции перевода.
    """

    operation: OperationDict


class MakePurchaseOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции покупки.
    """

    status: str
    amount: float
    cardId: str
    accountId: str
    category: str


class MakePurchaseOperationResponseDict(TypedDict):
    """
    Описание структуры ответа по созданию операции покупки.
    """

    operation: OperationDict


class MakeBillPaymentOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции оплаты по счету.
    """

    status: str
    amount: float
    cardId: str
    accountId: str


class MakeBillPaymentOperationResponseDict(TypedDict):
    """
    Описание структуры ответа по позданию операции оплаты по счету.
    """

    operation: OperationDict


class MakeCashWithdrawalOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции снятия наличных.
    """

    status: str
    amount: float
    cardId: str
    accountId: str


class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """
    Описание структуры ответа по созданию операции снятия наличных.
    """

    operation: OperationDict


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def __init__(self, client):
        super().__init__(client)
        self.operations_api = "/api/v1/operations"

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка операций счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response с данными об операциях.
        """

        return self.get(self.operations_api, params=QueryParams(**query))

    def get_operations_summary_api(
        self, query: GetOperationsSummaryQueryDict
    ) -> Response:
        """
        Выполняет GET-запрос на получение статистики по операциям счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response с данными об операциях.
        """

        return self.get(
            f"{self.operations_api}/operations-summary", params=QueryParams(**query)
        )

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение чека по операции.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """

        return self.get(f"{self.operations_api}/operation-receipt/{operation_id}")

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации по операции.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """

        return self.get(f"{self.operations_api}/{operation_id}")

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции комиссии.

        :param request: Словарь с данными операции комиссии.
        :return: Объект httpx.Response с результатом операции.
        """

        return self.post(f"{self.operations_api}/make-fee-operation", json=request)

    def make_top_up_operation_api(
        self, request: MakeTopUpOperationRequestDict
    ) -> Response:
        """
        Выполняет POST-запрос для создания операции пополнения.

        :param request: Словарь с данными операции пополнения.
        :return: Объект httpx.Response с результатом операции.
        """

        return self.post(f"{self.operations_api}/make-top-up-operation", json=request)

    def make_cashback_operation_api(
        self, request: MakeCashbackOperationRequestDict
    ) -> Response:
        """
        Выполняет POST-запрос для создания операции кэшбэка.

        :param request: Словарь с данными операции кэшбэка.
        :return: Объект httpx.Response с результатом операции.
        """

        return self.post(f"{self.operations_api}/make-cashback-operation", json=request)

    def make_transfer_operation_api(
        self, request: MakeTransferOperationRequestDict
    ) -> Response:
        """
        Выполняет POST-запрос для создания операции перевода.

        :param request: Словарь с данными операции перевода.
        :return: Объект httpx.Response с результатом операции.
        """

        return self.post(f"{self.operations_api}/make-transfer-operation", json=request)

    def make_purchase_operation_api(
        self, request: MakePurchaseOperationRequestDict
    ) -> Response:
        """
        Выполняет POST-запрос для создания операции покупки.

        :param request: Словарь с данными операции покупки.
        :return: Объект httpx.Response с результатом операции.
        """

        return self.post(f"{self.operations_api}/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(
        self, request: MakeBillPaymentOperationRequestDict
    ) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты по счету.

        :param request: Словарь с данными операции оплаты по счету.
        :return: Объект httpx.Response с результатом операции.
        """

        return self.post(
            f"{self.operations_api}/make-bill-payment-operation", json=request
        )

    def make_cash_withdrawal_operation_api(
        self, request: MakeCashWithdrawalOperationRequestDict
    ) -> Response:
        """
        Выполняет POST-запрос для создания операции снятия наличных.

        :param request: Словарь с данными операции снятия наличных денег.
        :return: Объект httpx.Response с результатом операции.
        """

        return self.post(
            f"{self.operations_api}/make-cash-withdrawal-operation",
            json=request,
        )

    def get_operations(self, account_id) -> GetOperationsResponseDict:
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query=query)
        return response.json()

    def get_operations_summary(self, account_id) -> GetOperationsSummaryResponseDict:
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query=query)
        return response.json()

    def get_operation_receipt(self, operation_id) -> GetOperationReceiptResponseDict:
        response = self.get_operation_receipt_api(operation_id=operation_id)
        return response.json()

    def get_operation(self, operation_id) -> GetOperationResponseDict:
        response = self.get_operation_api(operation_id=operation_id)
        return response.json()

    def make_fee_operation(
        self, card_id: str, account_id: str
    ) -> MakeFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(
        self, card_id: str, account_id: str
    ) -> MakeTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=50000.00,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(
        self, card_id: str, account_id: str
    ) -> MakeCashbackOperationResponseDict:
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=69.99,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(
        self, card_id: str, account_id: str
    ) -> MakeTransferOperationResponseDict:
        request = MakeTransferOperationRequestDict(
            status="IN_PROGRESS",
            amount=15000.00,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(
        self, card_id: str, account_id: str
    ) -> MakePurchaseOperationResponseDict:
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=3499.90,
            cardId=card_id,
            accountId=account_id,
            category="marketplace",
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(
        self, card_id: str, account_id: str
    ) -> MakeBillPaymentOperationResponseDict:
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=4200.00,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(
        self, card_id: str, account_id: str
    ) -> MakeCashWithdrawalOperationResponseDict:
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=10000.00,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient
    с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
