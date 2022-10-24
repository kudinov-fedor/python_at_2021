import os
import requests


class ApiClient:
    host = "https://demoqa.com"

    def __init__(self):
        self.client = requests.Session()
        self.payload = {
            "userName": os.environ["USER_NAME"],
            "password": os.environ["PASSWORD"]
        }
        self.user_id = None

    def set_token(self, token):
        self.client.headers["Authorization"] = f"Bearer {token}"

    def create_user(self):
        res = self.client.post(url=self.host + "/Account/v1/User", json=self.payload)
        return res

    def generate_token(self):
        res = self.client.post(url=self.host + "/Account/v1/GenerateToken", json=self.payload)
        return res

    def login(self):
        res = self.client.post(url=self.host + "/Account/v1/Login", json=self.payload)
        return res

    def set_user_id(self, user_id):
        self.user_id = user_id

    def check_authorization(self):
        res = self.client.post(url=self.host + "/Account/v1/Authorized",
                               json=self.payload)
        return res

    def get_user(self):
        res = self.client.get(url=self.host + f"/Account/v1/User/{self.user_id}", json=self.payload)
        return res

    def get_books(self):
        res = self.client.get(url=self.host + "/BookStore/v1/Books")
        return res

    def get_book(self, isbn: str):
        query_params = {"ISBN": isbn}
        res = self.client.get(url=self.host + f"/BookStore/v1/Book",
                              params=query_params)
        return res

    def add_book_to_collection(self, isbn: str):
        json = {"userId": f"{self.user_id}", "collectionOfIsbns": [
            {"isbn": f"{isbn}"}]}
        res = self.client.post(url=self.host + "/BookStore/v1/Books", json=json)
        return res

    def change_book_in_collection(self, isbn: str):
        json = {"userId": f"{self.user_id}", "isbn": f"{isbn}"}
        res = self.client.put(url=self.host + f"/BookStore/v1/Books/{isbn}", json=json)
        return res

    def delete_book(self, isbn: str):
        json = {"userId": f"{self.user_id}", "isbn": f"{isbn}"}
        res = self.client.delete(url=self.host + "/BookStore/v1/Book", json=json)
        return res

    def delete_all_books(self):
        query_params = {"UserId": self.user_id}
        res = self.client.delete(url=self.host + f"/BookStore/v1/Books", params=query_params)
        return res

    def delete_user(self):
        res = self.client.delete(url=self.host + f"/Account/v1/User/{self.user_id}")
        return res

    # Custom methods used for set up and tear down
    def prepare_token(self):
        res = self.generate_token()
        self.set_token(res.json()["token"])
        return self

    def prepare_user(self):
        res = self.login()
        self.set_user_id(res.json()["userId"])
        return self

    def remove_user_id(self):
        self.user_id = None
