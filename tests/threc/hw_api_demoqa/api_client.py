from requests import session


class ApiClient:
    host = "https://demoqa.com"

    def __init__(self, login, password):
        self.login = login
        self.user_id = None
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
        self.token = self.generate_token()["token"]

        self.user_id = res.json()["userId"]
        res.raise_for_status()
        return res.json()

    def create_user(self):
        res = self.client.post(self.host + "/Account/v1/User",
                               json={"userName": self.login,
                                     "password": self.password})
        self.token = self.generate_token()["token"]
        self.user_login()
        self.user_id = self.user_login()["userId"]

        res.raise_for_status()
        return res.json()

    def generate_token(self):
        res = self.client.post(self.host + "/Account/v1/GenerateToken",
                               json={"userName": self.login,
                                     "password": self.password})
        res.raise_for_status()
        return res.json()

    def get_book(self, isbn: str):
        res = self.client.get(self.host + "/BookStore/v1/Book", params={"ISBN": isbn})
        res.raise_for_status()
        return res.json()

    def get_books(self):
        res = self.client.get(self.host + "/BookStore/v1/Books", headers=self.client.headers)
        res.raise_for_status()
        return res.json()

    def get_profile(self):
        res = self.client.get(self.host + f"/Account/v1/User/{self.user_id}", headers=self.client.headers)
        res.raise_for_status()
        return res.json()

    def add_books(self, isbn: str):
        payload = {
            "userId": self.user_id,
            "collectionOfIsbns": [{"isbn": isbn}]
        }
        res = self.client.post(self.host + f"/BookStore/v1/Books",
                               json=payload,
                               headers=self.client.headers)
        res.raise_for_status()
        return res.json()

    def delete_book(self, isbn: str):
        payload = {
            "isbn": isbn,
            "userId": self.user_id
        }
        res = self.client.delete(self.host + f"/BookStore/v1/Book",
                                 json=payload,
                                 headers=self.client.headers)
        res.raise_for_status()

    def delete_books(self):
        params = {"UserId": self.user_id}
        res = self.client.delete(self.host + f"/BookStore/v1/Books", params=params,
                                 headers=self.client.headers)
        res.raise_for_status()
