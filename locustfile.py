from locust import HttpUser, TaskSet, task, between
import random

class UserBehavior(HttpUser):
    wait_time = between(20,50)

    @task(1)
    def index(self):
        self.client.get("/simulate")