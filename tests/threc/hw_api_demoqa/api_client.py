import pytest
from requests import session
from tests.threc.hw_api_demoqa.constants import Site


class ApiClient:
    host = "https://demoqa.com"

    def __init__(self, login, password):
        self.login = login
        self.user_id = Site.USER_ID
        self.password = password
        self.client = session()

    @property
    def token(self):
        header = self.client.headers.get("Authorization")
        return header.replace("Bearer ", "") if header else None

    @token.setter
    def token(self, token):
        if token:
            self.client.headers["Authorization"] = "Bearer {}".format(token)
        else:
            del self.token

    @token.deleter
    def token(self):
        self.client.headers.pop("Authorization", None)

    def user_login(self):
        res = self.client.post(self.host + "/Account/v1/Login",
                               json={"userName": self.login,
                                     "password": self.password})
        res.raise_for_status()
        return res.json()

    @property
    def generate_token(self):
        res = self.client.post(self.host + "/Account/v1/GenerateToken",
                               json={"userName": self.login,
                                     "password": self.password})
        res.raise_for_status()
        return res.json()

    def get_book(self, isbn: str):
        response = self.user_login()
        # headers = {"Authorization": f"Bearer {response['token']}"}
        res = self.client.get(self.host + "/BookStore/v1/Book", params={"ISBN": isbn}, headers=self.client.headers)
        res.raise_for_status()
        return res.json()

    def get_books(self):
        # response = self.user_login()
        # headers = {"Authorization": f"Bearer {response['token']}"}
        res = self.client.get(self.host + "/BookStore/v1/Books", headers=self.client.headers)
        res.raise_for_status()
        return res.json()

    def get_profile(self):
        assert self.user_id
        response = self.user_login()
        headers = {"Authorization": f"Bearer {response['token']}"}
        res = self.client.get(self.host + f"/Account/v1/User/{self.user_id}", headers=headers)
        res.raise_for_status()
        return res.json()

    def add_books(self, isbn: str):
        response = self.user_login()
        headers = {"Authorization": f"Bearer {response['token']}"}
        payload = {
            "userId": response['userId'],
            "collectionOfIsbns": [{"isbn": isbn}]
        }
        res = self.client.post(self.host + f"/BookStore/v1/Books",
                               json=payload,
                               headers=headers)
        res.raise_for_status()
        return res.json()

    def delete_book(self, isbn: str):
        response = self.user_login()
        headers = {"Authorization": f"Bearer {response['token']}"}
        payload = {
            "isbn": isbn,
            "userId": response['userId']
        }
        res = self.client.delete(self.host + f"/BookStore/v1/Book",
                                 json=payload,
                                 headers=headers)
        res.raise_for_status()

    def delete_books(self):
        response = self.user_login()
        headers = {"Authorization": f"Bearer {response['token']}"}
        params = {"UserId": response['userId']}
        res = self.client.delete(self.host + f"/BookStore/v1/Books", params=params,
                                 headers=headers)
        res.raise_for_status()
