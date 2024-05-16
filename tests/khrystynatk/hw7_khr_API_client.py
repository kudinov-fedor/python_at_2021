from requests import session
from tests.khrystynatk import hw7_khr_Constants as Const


class ApiClient:
    HOST = Const.HOST

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
    def token(self, token):
        if token:
            self.session.headers["Authorization"] = "Bearer {}".format(token)
        else:
            del self.token

    @token.deleter
    def token(self):
        self.session.headers.pop("Authorization", None)

    def generate_token(self):
        res = self.session.post(self.HOST + "/Account/v1/GenerateToken",
                                json={"userName": self.login,
                                      "password": self.password})
        res.raise_for_status()
        return res.json()

    def user_exists(self):
        res = self.session.post(self.HOST + "/Account/v1/Authorized",
                                json={"userName": self.login,
                                      "password": self.password})
        return res.status_code == 200

    def create_user(self):
        if not self.user_exists():
            res = self.session.post(self.HOST + "/Account/v1/User",
                                    json={"userName": self.login,
                                          "password": self.password})
            self.token = self.generate_token()["token"]
            self.login_user()
            self.user_id = self.login_user()["userId"]

            res.raise_for_status()
            return res.json()

    def user_is_authorized(self):
        res = self.session.post(self.HOST + "/Account/v1/Authorized",
                                json={"userName": self.login,
                                      "password": self.password})
        res.raise_for_status()
        return res.content == "true"

    def login_user(self):
        res = self.session.post(self.HOST + "/Account/v1/Login",
                                json={"userName": self.login,
                                      "password": self.password})
        res.raise_for_status()
        return res.json()

    def get_user(self):
        res = self.session.get(self.HOST + "/Account/v1/User/{}".format(self.user_id))

        res.raise_for_status()
        return res.json()

    def delete_user(self):
        res = self.session.delete(self.HOST + "/Account/v1/User/{}".format(self.user_id))

        res.raise_for_status()
        return res.status_code

    def get_books(self):
        res = self.session.get(self.HOST + "/BookStore/v1/Books")
        books = res.json()['books']

        return books

    def get_book(self, isbn):
        res = self.session.get(self.HOST + "/BookStore/v1/Book?ISBN={}".format(isbn))
        res.raise_for_status()
        return res.json()

    def add_book(self, isbn):
        res = self.session.post(self.HOST + "/BookStore/v1/Books", json={"userId": self.user_id,
                                                                         "collectionOfIsbns": [{"isbn": isbn}]})
        res.raise_for_status()
        return res.json()

    def change_book(self, isbn, isbn2):
        res = self.session.put(self.HOST + "/BookStore/v1/Books/{}".format(isbn),
                               json={"userId": self.user_id,
                                     "isbn": isbn2})

        res.raise_for_status()
        return res.json()

    def delete_book(self, isbn):
        res = self.session.delete(self.HOST + "/BookStore/v1/Book", json={"isbn": isbn,
                                                                          "userId": self.user_id})
        res.raise_for_status()

    def delete_books(self):
        res = self.session.delete(self.HOST + "/BookStore/v1/Books?UserId={}".format(self.user_id))
        res.raise_for_status()

    def reset_user(self):
        res = self.generate_token()
        self.token = res["token"]
        self.delete_user()
        self.user_id = None
        self.token = None
