from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class DocumentDict(TypedDict):
    """Описание структуры документа"""

    url: str
    document: bytes


class GetTariffDocumentResponseDict(TypedDict):
    """Описание структуры ответа на запрос документа тарифа по счету"""

    tariff: DocumentDict


class GetContractDocumentResponseDict(TypedDict):
    """Описание структуры ответа на запрос документа контракта по счету"""

    contract: DocumentDict


class DocumentGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/documents сервиса http-gateway.
    """

    def get_tariff_document_api(self, account_id: str) -> Response:
        """
        Получение тарифа по счету.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/documents/tariff-document/{account_id}")

    def get_contract_document_api(self, account_id: str) -> Response:
        """
        Получение контракта по счету.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/documents/contract-document/{account_id}")

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseDict:
        response = self.get_tariff_document_api(account_id)
        return response.json()

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseDict:
        response = self.get_contract_document_api(account_id)
        return response.json()


def build_documents_http_client() -> DocumentGatewayHTTPClient:
    """
    Функция создаёт экземпляр DocumentsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию DocumentsGatewayHTTPClient.
    """
    return DocumentGatewayHTTPClient(client=build_gateway_http_client())
