from httpx import Response
from locust.env import Environment

from clients.http.client import HTTPClient, HTTPClientExtensions
from clients.http.gateway.client import (
    build_gateway_http_client,
    build_gateway_locust_http_client,
)
from clients.http.gateway.documents.schema import (
    GetTariffDocumentResponseSchema,
    GetContractDocumentResponseSchema,
)


class DocumentsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/documents сервиса http-gateway.
    """

    def __init__(self, client):
        super().__init__(client)
        self.documents_api = "/api/v1/documents"

    def get_tariff_document_api(self, account_id: str) -> Response:
        """
        Получение тарифа по счету.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(
            f"{self.documents_api}/tariff-document/{account_id}",
            extensions=HTTPClientExtensions(
                route=self.documents_api + "/tariff-document/{account_id}"
            ),
        )

    def get_contract_document_api(self, account_id: str) -> Response:
        """
        Получение контракта по счету.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(
            f"{self.documents_api}/contract-document/{account_id}",
            extensions=HTTPClientExtensions(
                route=self.documents_api + "/contract-document/{account_id}"
            ),
        )

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseSchema:
        response = self.get_tariff_document_api(account_id)
        return GetTariffDocumentResponseSchema.model_validate_json(response.text)

    def get_contract_document(
        self, account_id: str
    ) -> GetContractDocumentResponseSchema:
        response = self.get_contract_document_api(account_id)
        return GetContractDocumentResponseSchema.model_validate_json(response.text)


def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    """
    Функция создаёт экземпляр DocumentsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию DocumentsGatewayHTTPClient.
    """
    return DocumentsGatewayHTTPClient(client=build_gateway_http_client())


def build_documents_gateway_locust_http_client(
    environment: Environment,
) -> DocumentsGatewayHTTPClient:
    """
    Функция создаёт экземпляр DocumentsGatewayHTTPClient, адаптированного под Locust.

    Клиент автоматически собирает метрики и передаёт их в Locust через хуки.
    Используется исключительно в нагрузочных тестах.

    :param environment: Объект окружения Locust.
    :return: экземпляр DocumentsGatewayHTTPClient с хуками сбора метрик.
    """
    return DocumentsGatewayHTTPClient(
        client=build_gateway_locust_http_client(environment)
    )
