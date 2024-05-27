from requests import session
from tests.yspryn.test_HW7_APItests import constants as Const


class ApiClient:
    host = Const.HOST

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.user_id = None
        self.client = session()

    @property
    def token(self):
        header = self.client.get("Authorization")
        return header.replace("Bearer", "") if header else None

    @token.setter
    def token(self, token):
        if token:
            self.client.headers["Authorization"] = "Bearer {}".format(token)
        else:
            del self.token

    @token.deleter
    def token(self):
        self.client.headers.pop("Authorization", None)

    def user_create(self):
        res = self.client.post(self.host + "/Account/v1/User",
                               json={"userName": self.login,
                                     "password": self.password})
        res.raise_for_status()
        return res.json()

    def generate_token(self):
        res = self.client.post(self.host + "/Account/v1/GenerateToken",
                               json={"userName": self.login,
                                     "password": self.password})
        res.raise_for_status()
        return res.json()

    def user_login(self):
        res = self.client.post(self.host + "/Account/v1/Authorized",
                               json={"userName": Const.USERNAME,
                                     "password": Const.PASSWORD})
        res.raise_for_status()
        return res.json()

    def get_user(self):
        res = self.client.get(self.host + "/Account/v1/User/{}".format(self.user_id))
        res.raise_for_status()
        return res.json()

    def get_books(self):
        res = self.client.get(self.host + "/BookStore/v1/Books")
        res.raise_for_status()
        return res.json()["books"]

    def add_book(self, isbn: str):
        res = self.client.post(self.host + "/BookStore/v1/Books",
                               json={"userId": self.user_id,
                                     "collectionOfIsbns": [{"isbn": isbn}]
                                     })
        res.raise_for_status()
        return res.json()

    def remove_book(self, isbn: str):
        res = self.client.delete(self.host + "/BookStore/v1/Book",
                                 json={"isbn": isbn,
                                       "userId": self.user_id})
        res.raise_for_status()
     
    def remove_books(self):
        res = self.client.delete(self.host + "/BookStore/v1/Books?UserId={}".format(self.user_id))
        res.raise_for_status()

    # --- high level API ---
    def setup_user(self, login: str, password: str):
        self.login = login
        self.password = password
        self.user_login()
        self.token = self.generate_token()["token"]
        self.user_id = Const.UserID
