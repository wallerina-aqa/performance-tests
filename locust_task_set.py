from locust import HttpUser, between, TaskSet, task, SequentialTaskSet


class BrowseCatalog(SequentialTaskSet):
    @task(3)
    def get_product(self):
        self.client.get("/product/12345")

    @task(2)
    def get_category(self):
        self.client.get("/category/45789")


class BrowseBucket(TaskSet):
    @task
    def get_bucket(self):
        self.client.get("/bucket")


class ShopUser(HttpUser):
    tasks = {
        BrowseCatalog: 3,
        BrowseBucket: 7,
    }
    wait_time = between(1, 3)
