from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.cards.schema import (
    IssueVirtualCardRequestSchema,
    IssuePhysicalCardRequestSchema,
    IssueVirtualCardResponseSchema,
    IssuePhysicalCardResponseSchema,
)
from clients.http.gateway.client import build_gateway_http_client


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """

    def __init__(self, client):
        super().__init__(client)
        self.cards_api = "/api/v1/cards"

    def issue_virtual_card_api(
        self, request: IssueVirtualCardRequestSchema
    ) -> Response:
        """
        Создание новой виртуальной карты.

        :param request: Словарь с идентификаторами пользователя и счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            f"{self.cards_api}/issue-virtual-card",
            json=request.model_dump(by_alias=True),
        )

    def issue_physical_card_api(
        self, request: IssuePhysicalCardRequestSchema
    ) -> Response:
        """
        Создание новой физической карты.

        :param request: Словарь с идентификаторами пользователя и счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            f"{self.cards_api}/issue-physical-card",
            json=request.model_dump(by_alias=True),
        )

    def issue_virtual_card(
        self, user_id: str, account_id: str
    ) -> IssueVirtualCardResponseSchema:
        request = IssueVirtualCardRequestSchema(user_id=user_id, account_id=account_id)
        response = self.issue_virtual_card_api(request=request)
        return IssueVirtualCardResponseSchema.model_validate_json(response.text)

    def issue_physical_card(
        self, user_id: str, account_id: str
    ) -> IssuePhysicalCardResponseSchema:
        request = IssuePhysicalCardRequestSchema(user_id=user_id, account_id=account_id)
        response = self.issue_physical_card_api(request)
        return IssuePhysicalCardResponseSchema.model_validate_json(response.text)


def build_cards_http_client() -> CardsGatewayHTTPClient:
    """
    Функция создаёт экземпляр CardsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CardsGatewayHTTPClient.
    """
    return CardsGatewayHTTPClient(client=build_gateway_http_client())
