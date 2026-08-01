from locust import HttpUser, between, task


class BasicScenarioUser(HttpUser):
    wait_time = between(5, 15)

    @task(2)
    def get_data(self):
        self.client.get("/get")

    @task
    def post_data(self):
        self.client.post("/post")

    @task
    def delete_data(self):
        self.client.delete("/delete")
