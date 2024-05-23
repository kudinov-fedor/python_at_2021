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

    def user_create(self):
        res = self.session.post(self.HOST + "/Account/v1/User",
                                json={"userName": self.login,
                                      "password": self.password})
        res.raise_for_status()
        return res.json()

    def generate_token(self):
        res = self.session.post(self.HOST + "/Account/v1/GenerateToken",
                                json={"userName": self.login,
                                      "password": self.password})
        res.raise_for_status()
        return res.json()

    def user_exists(self) -> bool:
        res = self.session.post(self.HOST + "/Account/v1/Authorized",
                                json={"userName": self.login,
                                      "password": self.password})
        return res.status_code == 200

    def user_login(self):
        res = self.session.post(self.HOST + "/Account/v1/Login",
                                json={"userName": self.login,
                                      "password": self.password})
        res.raise_for_status()
        return res.json()

    def user_get(self):
        res = self.session.get(self.HOST + "/Account/v1/User/{}".format(self.user_id))
        res.raise_for_status()
        return res.json()

    def books_get(self):
        res = self.session.get(self.HOST + "/BookStore/v1/Books")
        res.raise_for_status()
        return res.json()

    def books_add(self, isbn):
        data = {"userId": self.user_id,
                "collectionOfIsbns": [{"isbn": isbn}]}
        res = self.session.post(self.HOST + "/BookStore/v1/Books", json=data)
        res.raise_for_status()
        return res.json()

    def books_delete(self, isbn):
        params = {"UserId": self.user_id}
        res = self.session.delete(self.HOST + "/BookStore/v1/Books", params=params)
        res.raise_for_status()

    def user_delete(self):
        res = self.session.delete(self.HOST + "/Account/v1/User/{}".format(self.user_id))
        res.raise_for_status()

    def create(self):
        if self.user_exists():
            user = self.user_login()
            self.user_id = user["userId"]
            self.token = user["token"] or self.generate_token()["token"]
            self.reset()

        self.user_id = self.user_create()["userID"]
        self.token = self.generate_token()["token"]

    def update_token(self):
        res = self.generate_token()
        self.token = res["token"]

    def reset(self):
        self.update_token()
        self.user_delete()
        self.token = None
        self.user_id = None
