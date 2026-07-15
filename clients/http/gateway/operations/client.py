from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.operations.schema import (
    GetOperationsQuerySchema,
    GetOperationsSummaryQuerySchema,
    MakeFeeOperationRequestSchema,
    MakeTopUpOperationRequestSchema,
    MakeCashbackOperationRequestSchema,
    MakeTransferOperationRequestSchema,
    MakePurchaseOperationRequestSchema,
    MakeBillPaymentOperationRequestSchema,
    MakeCashWithdrawalOperationRequestSchema,
    GetOperationsResponseSchema,
    GetOperationsSummaryResponseSchema,
    GetOperationReceiptResponseSchema,
    GetOperationResponseSchema,
    MakeFeeOperationResponseSchema,
    OperationStatus,
    MakeTopUpOperationResponseSchema,
    MakeCashbackOperationResponseSchema,
    MakeTransferOperationResponseSchema,
    MakePurchaseOperationResponseSchema,
    MakeBillPaymentOperationResponseSchema,
    MakeCashWithdrawalOperationResponseSchema,
)


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def __init__(self, client):
        super().__init__(client)
        self.operations_api = "/api/v1/operations"

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Выполняет GET-запрос на получение списка операций счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response с данными об операциях.
        """

        return self.get(
            self.operations_api, params=QueryParams(**query.model_dump(by_alias=True))
        )

    def get_operations_summary_api(
        self, query: GetOperationsSummaryQuerySchema
    ) -> Response:
        """
        Выполняет GET-запрос на получение статистики по операциям счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response с данными об операциях.
        """

        return self.get(
            f"{self.operations_api}/operations-summary",
            params=QueryParams(**query.model_dump(by_alias=True)),
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

    def make_fee_operation_api(
        self, request: MakeFeeOperationRequestSchema
    ) -> Response:
        """
        Выполняет POST-запрос для создания операции комиссии.

        :param request: Словарь с данными операции комиссии.
        :return: Объект httpx.Response с результатом операции.
        """

        return self.post(
            f"{self.operations_api}/make-fee-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_top_up_operation_api(
        self, request: MakeTopUpOperationRequestSchema
    ) -> Response:
        """
        Выполняет POST-запрос для создания операции пополнения.

        :param request: Словарь с данными операции пополнения.
        :return: Объект httpx.Response с результатом операции.
        """

        return self.post(
            f"{self.operations_api}/make-top-up-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_cashback_operation_api(
        self, request: MakeCashbackOperationRequestSchema
    ) -> Response:
        """
        Выполняет POST-запрос для создания операции кэшбэка.

        :param request: Словарь с данными операции кэшбэка.
        :return: Объект httpx.Response с результатом операции.
        """

        return self.post(
            f"{self.operations_api}/make-cashback-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_transfer_operation_api(
        self, request: MakeTransferOperationRequestSchema
    ) -> Response:
        """
        Выполняет POST-запрос для создания операции перевода.

        :param request: Словарь с данными операции перевода.
        :return: Объект httpx.Response с результатом операции.
        """

        return self.post(
            f"{self.operations_api}/make-transfer-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_purchase_operation_api(
        self, request: MakePurchaseOperationRequestSchema
    ) -> Response:
        """
        Выполняет POST-запрос для создания операции покупки.

        :param request: Словарь с данными операции покупки.
        :return: Объект httpx.Response с результатом операции.
        """

        return self.post(
            f"{self.operations_api}/make-purchase-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_bill_payment_operation_api(
        self, request: MakeBillPaymentOperationRequestSchema
    ) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты по счету.

        :param request: Словарь с данными операции оплаты по счету.
        :return: Объект httpx.Response с результатом операции.
        """

        return self.post(
            f"{self.operations_api}/make-bill-payment-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_cash_withdrawal_operation_api(
        self, request: MakeCashWithdrawalOperationRequestSchema
    ) -> Response:
        """
        Выполняет POST-запрос для создания операции снятия наличных.

        :param request: Словарь с данными операции снятия наличных денег.
        :return: Объект httpx.Response с результатом операции.
        """

        return self.post(
            f"{self.operations_api}/make-cash-withdrawal-operation",
            json=request.model_dump(by_alias=True),
        )

    def get_operations(self, account_id) -> GetOperationsResponseSchema:
        query = GetOperationsQuerySchema(account_id=account_id)
        response = self.get_operations_api(query=query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id) -> GetOperationsSummaryResponseSchema:
        query = GetOperationsSummaryQuerySchema(account_id=account_id)
        response = self.get_operations_summary_api(query=query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id) -> GetOperationReceiptResponseSchema:
        response = self.get_operation_receipt_api(operation_id=operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operation(self, operation_id) -> GetOperationResponseSchema:
        response = self.get_operation_api(operation_id=operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def make_fee_operation(
        self, card_id: str, account_id: str
    ) -> MakeFeeOperationResponseSchema:
        request = MakeFeeOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=55.77,
            card_id=card_id,
            account_id=account_id,
        )
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(
        self, card_id: str, account_id: str
    ) -> MakeTopUpOperationResponseSchema:
        request = MakeTopUpOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=50000.00,
            card_id=card_id,
            account_id=account_id,
        )
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(
        self, card_id: str, account_id: str
    ) -> MakeCashbackOperationResponseSchema:
        request = MakeCashbackOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=69.99,
            card_id=card_id,
            account_id=account_id,
        )
        response = self.make_cashback_operation_api(request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(
        self, card_id: str, account_id: str
    ) -> MakeTransferOperationResponseSchema:
        request = MakeTransferOperationRequestSchema(
            status=OperationStatus.IN_PROGRESS,
            amount=15000.00,
            card_id=card_id,
            account_id=account_id,
        )
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(
        self, card_id: str, account_id: str
    ) -> MakePurchaseOperationResponseSchema:
        request = MakePurchaseOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=3499.90,
            card_id=card_id,
            account_id=account_id,
            category="marketplace",
        )
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(
        self, card_id: str, account_id: str
    ) -> MakeBillPaymentOperationResponseSchema:
        request = MakeBillPaymentOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=4200.00,
            card_id=card_id,
            account_id=account_id,
        )
        response = self.make_bill_payment_operation_api(request)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(
        self, card_id: str, account_id: str
    ) -> MakeCashWithdrawalOperationResponseSchema:
        request = MakeCashWithdrawalOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=10000.00,
            card_id=card_id,
            account_id=account_id,
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(
            response.text
        )


def build_operations_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient
    с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
