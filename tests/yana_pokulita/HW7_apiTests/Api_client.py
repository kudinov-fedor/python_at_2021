from requests import session
from tests.yana_pokulita.HW7_apiTests import Constants as Const


class ApiClient:
    URL = Const.URL

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.session = session()
        self.user_id = None

    @property
    def token(self):
        header = self.session.headers.get("Authorization")
        return header.replace("Bearer ", "") if header else None

    @token.setter
    def token(self, token):
        if token:
            self.session.headers["Authorization"] = "Bearer {}".format(token)
        else:
            del self.token

    @token.deleter
    def token(self):
        self.session.headers.pop("Authorization", None)

    def generate_token(self):
        res = self.session.post(self.URL + "/Account/v1/GenerateToken",
                                json={"userName": self.login,
                                      "password": self.password})
        res.raise_for_status()
        return res.json()

    def login_user(self):
        res = self.session.post(self.URL + "/Account/v1/Login",
                                json={"userName": self.login,
                                      "password": self.password})
        res.raise_for_status()
        return res.json()

    def create_user(self):
        res = self.session.post(self.URL + "/Account/v1/User",
                                json={"userName": self.login,
                                      "password": self.password})
        return res.json()

    def get_profile(self):
        res = self.session.get(self.URL + f"/Account/v1/User/{self.user_id}")
        res.raise_for_status()
        return res.json()

    def get_books(self):
        res = self.session.get(self.URL + "/BookStore/v1/Books")
        res.raise_for_status()
        return res.json()

    def get_book(self, isbn):
        res = self.session.get(self.URL + "/BookStore/v1/Book", params={"ISBN": isbn})
        res.raise_for_status()
        return res.json()

    def add_book(self, isbn):
        payload = {
            "userId": self.user_id,
            "collectionOfIsbns": [{"isbn": isbn}]
        }
        res = self.session.post(self.URL + f"/BookStore/v1/Books", json=payload)
        res.raise_for_status()
        return res.json()

    def change_book(self, isbn, isbn2):
        res = self.session.put(self.URL + "/BookStore/v1/Books/{}".format(isbn),
                               json={"userId": self.user_id,
                                     "isbn": isbn2})

        res.raise_for_status()
        return res.json()

    def delete_book(self, isbn):
        res = self.session.delete(self.URL + "/BookStore/v1/Book", json={"isbn": isbn,
                                                                         "userId": self.user_id})
        res.raise_for_status()

    def delete_books(self):
        res = self.session.delete(self.URL + "/BookStore/v1/Books?UserId={}".format(self.user_id))
        res.raise_for_status()

    def setup_user(self):
        self.token = self.login_user()["token"]
        self.user_id = self.login_user()["userId"]
