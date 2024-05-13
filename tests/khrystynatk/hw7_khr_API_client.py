from requests import session


class ApiClient:
    HOST = "https://demoqa.com"

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

    def existing_user(self):
        res = self.session.post(self.HOST + "/Account/v1/User",
                                json={"userName": self.login,
                                      "password": self.password})
        return res.status_code == 406

    def create_user(self):
        if self.existing_user():
            self.token = self.generate_token()["token"]
            self.login_user()
            self.user_id = self.login_user()["userId"]

        else:
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
        res.raise_for_status()
        return res.json()

    def get_some_book(self, get_books, index):
        res = self.session.get(self.HOST + "/BookStore/v1/Book?ISBN={}".format(get_books[index]["isbn"]))
        res.raise_for_status()
        return res.json()

    def add_some_book(self, isbn):
        res = self.session.post(self.HOST + "/BookStore/v1/Books", json={"userId": self.user_id,
                                                                         "collectionOfIsbns": [{"isbn": isbn}]})
        res.raise_for_status()
        return res.json()

    def get_token(self):
        res = self.generate_token()
        self.token = res["token"]

    def reset_user(self):
        self.get_token()
        self.delete_user()
        self.token = None
