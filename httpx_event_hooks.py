from datetime import datetime

from httpx import Client, Request, Response


def log_request(request: Request):
    request.extensions["start_time"] = datetime.now()
    print(f"REQUEST: {request.method}")


def log_response(response: Response):
    duration = datetime.now() - response.request.extensions["start_time"]
    print(f"RESPONSE: {response.status_code}, {duration}")


client = Client(
    base_url="http://localhost:8003",
    event_hooks={"request": [log_request], "response": [log_response]},
)
response = client.get("/api/v1/users/1be37941-6ab6-4781-84e1-23c5e4fded8e")
print(response)
