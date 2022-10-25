import requests


class ApiClient:
    host = "https://demoqa.com"

    def __init__(self, user_name, password):
        self.client = requests.Session()
        self.user_id = None
        self.user_name = user_name
        self.password = password

    def set_token(self, token):
        self.client.headers["Authorization"] = f"Bearer {token}"

    def create_user(self):
        payload = {
            "userName": self.user_name,
            "password": self.password
        }
        res = self.client.post(url=self.host + "/Account/v1/User", json=payload)
        return res

    def generate_token(self):
        payload = {
            "userName": self.user_name,
            "password": self.password
        }
        res = self.client.post(url=self.host + "/Account/v1/GenerateToken", json=payload)
        return res

    def login(self):
        payload = {
            "userName": self.user_name,
            "password": self.password
        }
        res = self.client.post(url=self.host + "/Account/v1/Login", json=payload)
        return res

    def check_authorization(self):
        payload = {
            "userName": self.user_name,
            "password": self.password
        }
        res = self.client.post(url=self.host + "/Account/v1/Authorized",
                               json=payload)
        return res

    def get_user(self):
        payload = {
            "userName": self.user_name,
            "password": self.password
        }
        res = self.client.get(url=self.host + f"/Account/v1/User/{self.user_id}", json=payload)
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
        self.user_id = res.json()["userId"]
        return self
