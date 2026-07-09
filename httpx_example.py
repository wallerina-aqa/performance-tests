import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(response.json())
print(response.text)
print("-------------------------------------------------------------------")

data = {"title": "Новая задача", "completed": False, "userId": 1}
response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
print(response.status_code)
print(response.json())
print("-------------------------------------------------------------------")

headers = {"Authorization": "Bearer my_secret_token"}
response = httpx.get("https://httpbin.org/get", headers=headers)
print(response.status_code)
print(response.request.headers)
print(response.headers)
print(response.json())
print("-------------------------------------------------------------------")

params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(response.url)
print(response.request.url.query)
print(response.status_code)
print(response.json())
print("-------------------------------------------------------------------")

files = {"file": ("example.txt", open("example.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files=files)
print(response.status_code)
print(response.json())
print("-------------------------------------------------------------------")

with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
print(response1.json())
print(response2.json())
print("-------------------------------------------------------------------")

client = httpx.Client(
    base_url="https://jsonplaceholder.typicode.com",
    headers={"Authorization": "Bearer my_secret_token"},
)
response1 = client.get("/todos/1")
response2 = client.get("/todos/2")
print(response1.request.headers)
print(response1.json())
print(response2.request.headers)
print(response2.json())
client.close()
print("-------------------------------------------------------------------")

try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    print(response.status_code)
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")
print("-------------------------------------------------------------------")

try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
    print(response.status_code)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")
