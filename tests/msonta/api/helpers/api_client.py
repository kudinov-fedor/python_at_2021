import os
import requests


class ApiClient:
    host = "https://demoqa.com"

    def __init__(self):
        self.client = requests.session()
        self.payload = {
            "userName": os.environ["USER_NAME"],
            "password": os.environ["PASSWORD"]
        }
        self.user_id = None
        self.token = None

    def create_user(self):
        res = self.client.post(url=self.host + "/Account/v1/User",
                               json=self.payload)
        return res

    def generate_token(self):
        res = self.client.post(url=self.host + "/Account/v1/GenerateToken",
                               json=self.payload)
        self.token = res.json()["token"]
        return res

    def login(self):
        res = self.client.post(url=self.host + "/Account/v1/Login",
                               json=self.payload)
        self.user_id = res.json()["userId"]
        return res

    def check_authorization(self):
        res = self.client.post(url=self.host + "/Account/v1/Authorized",
                               json=self.payload)
        return res

    def get_user(self, token, user_id):
        headers = {"Authorization": f"Bearer {token}"}
        res = self.client.get(url=self.host + f"/Account/v1/User/{user_id}",
                              headers=headers, json=self.payload)
        return res

    def get_books(self):
        res = self.client.get(url=self.host + "/BookStore/v1/Books")
        return res

    def get_book(self, isbn):
        query_params = {"ISBN": isbn}
        res = self.client.get(url=self.host + f"/BookStore/v1/Book",
                              params=query_params)
        return res

    def add_book_to_collection(self, isbn, token, user_id):
        headers = {"Authorization": f"Bearer {token}"}
        json = {"userId": f"{user_id}", "collectionOfIsbns": [
            {"isbn": f"{isbn}"}]}
        res = self.client.post(url=self.host + "/BookStore/v1/Books",
                               headers=headers, json=json)
        return res

    def change_book_in_collection(self, isbn, token, user_id):
        headers = {"Authorization": f"Bearer {token}"}
        json = {"userId": f"{user_id}", "isbn": f"{isbn}"}
        res = self.client.put(url=self.host + f"/BookStore/v1/Books/{isbn}",
                              headers=headers, json=json)
        return res

    def delete_book(self, token, user_id, isbn):
        headers = {"Authorization": f"Bearer {token}"}
        json = {"userId": f"{user_id}", "isbn": f"{isbn}"}
        res = self.client.delete(url=self.host + "/BookStore/v1/Book",
                                 headers=headers, json=json)
        return res

    def delete_all_books(self, token, user_id):
        headers = {"Authorization": f"Bearer {token}"}
        query_params = {"UserId": user_id}
        res = self.client.delete(url=self.host + f"/BookStore/v1/Books",
                                 headers=headers, params=query_params)
        return res

    def delete_user(self, token, user_id):
        headers = {"Authorization": f"Bearer {token}"}
        res = self.client.delete(url=self.host + f"/Account/v1/User/{user_id}",
                                 headers=headers)
        return res
