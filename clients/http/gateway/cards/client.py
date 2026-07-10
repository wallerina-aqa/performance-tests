from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient


class IssueCardRequestDict(TypedDict):
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """

    def __init__(self, client):
        super().__init__(client)
        self.cards_api = "/api/v1/cards"

    def issue_virtual_card_api(self, request: IssueCardRequestDict) -> Response:
        """
        Создание новой виртуальной карты.

        :param request: Словарь с идентификаторами пользователя и счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(f"{self.cards_api}/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: IssueCardRequestDict) -> Response:
        """
        Создание новой физической карты.

        :param request: Словарь с идентификаторами пользователя и счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(f"{self.cards_api}/issue-physical-card", json=request)
