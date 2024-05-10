from requests import session
from tests.threc.hw_api_demoqa.constants import Site


class ApiClient:
    host = "https://demoqa.com"

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.user_id = None
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

    def generate_token(self):
        res = self.client.post(self.host + "/Account/v1/GenerateToken",
                               json={"userName": self.login,
                                     "password": self.password})
        res.raise_for_status()
        return res.json()

    def get_book(self):
        res = self.client.get(self.host + "/BookStore/v1/Book?" + Site.ISBN,
                              json={})
        res.raise_for_status()
        return res.json()
