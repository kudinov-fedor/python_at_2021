from requests import session

from tests.mizo.constants import HOST2
from tests.mizo.constants import PASSWORD
from tests.mizo.generate_user_names import generate_next_username


class LocustApiClient:
    # - avoiding painful error "missing required params" in init

    host = HOST2

    def __init__(self):
        self.user_id = None
        self.client = session()
        self.login = generate_next_username()
        self.password = PASSWORD

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

    def user_create(self):

        res = self.client.post(HOST2 + "/Account/v1/User",
                               json={"userName": self.login,
                                     "password": self.password})
        res.raise_for_status()
        return res.json()

    def generate_token(self):
        res = self.client.post(HOST2 + "/Account/v1/GenerateToken",
                               json={"userName": self.login,
                                     "password": self.password})
        res.raise_for_status()
        return res.json()

    def user_login(self):
        res = self.client.post(HOST2 + "/Account/v1/Login",
                               json={"userName": self.login,
                                     "password": self.password})
        res.raise_for_status()
        return res.json()

    def user_authorized(self):
        res = self.client.post(HOST2 + "/Account/v1/Authorized",
                               json={"userName": self.login,
                                     "password": self.password})
        res.raise_for_status()
        return res.json()

    def get_all_books(self):
        res = self.client.get(HOST2 + "/BookStore/v1/Books")
        res.raise_for_status()
        return res.json()

    def add_book_to_collection(self, isbns):
        res = self.client.post(HOST2 + "/BookStore/v1/Books",
                               json={"userId": self.user_id,
                                     "collectionOfIsbns": [{"isbn": isbn} for isbn in isbns]})
        res.raise_for_status()
        return res.json()

    def update_book(self, isbn):
        url = f"{HOST2}/BookStore/v1/Books/{isbn}"
        json_data = {
            "userId": self.user_id,
            "isbn": isbn
        }
        res = self.client.put(url, json=json_data)
        return res

    def delete_book(self, isbn):
        res = self.client.delete(HOST2 + "/BookStore/v1/Book",
                                 json={"isbn": isbn,
                                       "userId": self.user_id})
        res.raise_for_status()
        return res

    def delete_all_books(self, user_id):
        url = f"{HOST2}/BookStore/v1/Books?UserId={user_id}"
        res = self.client.delete(url)
        res.raise_for_status()

    def user_books(self, userid):
        url = f"{HOST2}/Account/v1/User/{userid}"
        res = self.client.get(url)
        res.raise_for_status()
        return res.json()
