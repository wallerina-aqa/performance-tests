import time

from httpx import Request, Response, HTTPError, HTTPStatusError
from locust.env import Environment


def locust_request_event_hook(request: Request) -> None:
    """
    HTTPX event hook, вызываемый перед отправкой запроса.

    Сохраняет текущее время в `request.extensions["start_time"]`,
    чтобы потом использовать его для расчёта времени ответа.
    """

    request.extensions["start_time"] = time.perf_counter()


def locust_response_event_hook(environment: Environment):
    """
    Возвращает HTTPX event hook, вызываемый после получения ответа.

    Использует `request.extensions["start_time"]` для вычисления времени отклика.
    Извлекает route из `request.extensions["route"]`, если задан.
    Отправляет собранные метрики в `environment.events.request`,
                                         чтобы Locust мог агрегировать статистику.

    :param environment: Объект окружения Locust, через который отправляются метрики.
    :return: Функция-хук для HTTPX response event hook.
    """

    def inner(response: Response) -> None:
        exception: HTTPError | HTTPStatusError | None = None
        try:
            response = response.raise_for_status()
        except (HTTPError, HTTPStatusError) as error:
            exception = error

        request = response.request
        route = request.extensions.get("route", request.url.path)
        start_time = request.extensions.get("start_time", time.perf_counter())
        response_time = (time.perf_counter() - start_time) * 1000
        response_length = len(response.read())

        if environment.events is None:
            raise RuntimeError("Locust events are not initialized")

        environment.events.request.fire(
            name=f"{request.method} {route}",
            context=None,
            response=response,
            exception=exception,
            request_type="HTTP",
            response_time=response_time,
            response_length=response_length,
        )

    return inner
