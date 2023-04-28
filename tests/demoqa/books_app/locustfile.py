import random
from locust import HttpUser, between, task

from api_client_locust_compatible import ApiClient


# locust -f /Users/fkudi/PycharmProjects/python_at_2021/tests/demoqa/books_app/locustfile.py
# -H https://demoqa.com -u 1 -r 5 -t 300s --autostart -P 8089


class LocustClient(HttpUser, ApiClient):
    wait_time = between(1, 5)

    def on_start(self):
        self.login = f"test_{random.randint(0, 999999)}"
        self.password = "Test123!@#"
        self.create()

    def on_stop(self):
        self.reset()

    @task
    def task_books_get(self):
        self.books_get()

    @task
    def task_user_get(self):
        self.user_get()
