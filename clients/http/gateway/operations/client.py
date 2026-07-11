from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def __init__(self, client):
        super().__init__(client)
        self.operations_api = "/api/v1/operations"

    class GetOperationsQueryDict(TypedDict):
        """
        Структура данных для получения списка операций счета.
        """

        accountId: str

    class GetOperationsSummaryQueryDict(TypedDict):
        """
        Структура данных для получения статистики по операциям счета.
        """

        accountId: str

    class MakeFeeOperationRequestDict(TypedDict):
        """
        Структура данных для создания операции комиссии.
        """

        status: str
        amount: int
        cardId: str
        accountId: str

    class MakeTopUpOperationRequestDict(TypedDict):
        """
        Структура данных для создания операции пополнения.
        """

        status: str
        amount: int
        cardId: str
        accountId: str

    class MakeCashbackOperationRequestDict(TypedDict):
        """
        Структура данных для создания операции кэшбэка.
        """

        status: str
        amount: int
        cardId: str
        accountId: str

    class MakeTransferOperationRequestDict(TypedDict):
        """
        Структура данных для создания операции перевода.
        """

        status: str
        amount: int
        cardId: str
        accountId: str

    class MakePurchaseOperationRequestDict(TypedDict):
        """
        Структура данных для создания операции покупки.
        """

        status: str
        amount: int
        cardId: str
        accountId: str

    class MakeBillPaymentOperationRequestDict(TypedDict):
        """
        Структура данных для создания операции оплаты по счету.
        """

        status: str
        amount: int
        cardId: str
        accountId: str

    class MakeCashWithdrawalOperationRequestDict(TypedDict):
        """
        Структура данных для создания операции снятия наличных денег.
        """

        status: str
        amount: int
        cardId: str
        accountId: str

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
        Выполняет POST-запрос для создания операции снятия наличных денег.

        :param request: Словарь с данными операции снятия наличных денег.
        :return: Объект httpx.Response с результатом операции.
        """

        return self.post(
            f"{self.operations_api}/make-cash-withdrawal-operation",
            json=request,
        )
