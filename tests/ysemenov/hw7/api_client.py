from requests import session
from tests.ysemenov.hw7.constants import HOST


class ApiClient:

    HOST = HOST

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.user_id = None
        self.session = session()

    @property
    def token(self):
        header = self.session.headers.get("Authorization")
        return header.replace("Bearer ", "") if header else None

    @token.setter
    def token(self, token: str):
        if token:
            self.session.headers["Authorization"] = "Bearer {}".format(token)
        else:
            del self.token

    @token.deleter
    def token(self):
        self.session.headers.pop("Authorization", None)

    def create_user(self) -> dict:
        data = {"userName": self.login,
                "password": self.password}
        res = self.session.post(self.HOST + "/Account/v1/User", json=data)
        res.raise_for_status()
        return res.json()

    def generate_token(self) -> dict:
        data = {"userName": self.login,
                "password": self.password}
        res = self.session.post(self.HOST + "/Account/v1/GenerateToken", json=data)
        res.raise_for_status()
        return res.json()

    def user_exists(self) -> bool:
        data = {"userName": self.login,
                "password": self.password}
        res = self.session.post(self.HOST + "/Account/v1/Authorized", json=data)
        return res.status_code == 200

    def login_user(self) -> dict:
        data = {"userName": self.login,
                "password": self.password}
        res = self.session.post(self.HOST + "/Account/v1/Login", json=data)
        res.raise_for_status()
        return res.json()

    def get_user(self) -> dict:
        res = self.session.get(self.HOST + "/Account/v1/User/{}".format(self.user_id))
        res.raise_for_status()
        return res.json()

    def get_books(self) -> dict:
        res = self.session.get(self.HOST + "/BookStore/v1/Books")
        res.raise_for_status()
        return res.json()

    def get_book(self, isbn: str) -> dict:
        res = self.session.get(self.HOST + "/BookStore/v1/Book/{}".format(isbn))
        res.raise_for_status()
        return res.json()

    def add_book(self, isbn: str) -> dict:
        data = {"userId": self.user_id,
                "collectionOfIsbns": [{"isbn": isbn}]}
        res = self.session.post(self.HOST + "/BookStore/v1/Books", json=data)
        res.raise_for_status()
        return res.json()

    def replace_book(self, isbn1: str, isbn2: str) -> dict:
        data = {"userId": self.user_id,
                "isbn": isbn2}
        res = self.session.put(self.HOST + "/BookStore/v1/Books/{}".format(isbn1), json=data)
        res.raise_for_status()
        return res.json()

    def delete_book(self, isbn: str):
        data = {"isbn": isbn,
                "userId": self.user_id}
        res = self.session.delete(self.HOST + "/BookStore/v1/Book", json=data)
        res.raise_for_status()

    def delete_books(self):
        params = {"UserId": self.user_id}
        res = self.session.delete(self.HOST + "/BookStore/v1/Books", params=params)
        res.raise_for_status()

    def user_delete(self):
        res = self.session.delete(self.HOST + "/Account/v1/User/{}".format(self.user_id))
        res.raise_for_status()

    def create(self):
        if self.user_exists():
            user = self.login_user()
            self.user_id = user["userId"]
            self.reset()

        self.user_id = self.create_user()["userID"]
        self.token = self.update_token()

    def update_token(self):
        res = self.generate_token()
        self.token = res["token"]
        return self.token

    def reset(self):
        self.update_token()
        self.user_delete()
        self.token = None
        self.user_id = None
