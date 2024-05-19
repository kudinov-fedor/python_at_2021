from requests import session
from tests.mariana_petrushanska.test_api_hw7.constansts import General, User, Books


class ApiClient:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.user_id = None
        self.client = session()

    @property
    def token(self):
        header = self.client.headers.get("Authorization")
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

    def generate_token(self):
        res = self.client.post(General.GENERATE_TOKEN,
                                    json={"userName": self.login,
                                          "password": self.password})
        res.raise_for_status()
        return res.json()

    def user_login(self):
        res = self.client.post(User.USER_LOGIN,
                                    json={"userName": self.login,
                                          "password": self.password})
        res.raise_for_status()
        return res.json()

    def user_authorized(self):
        res = self.client.post(User.USER_AUTHORIZED,
                                    json={"userName": self.login,
                                          "password": self.password})
        res.raise_for_status()
        return res.json()

    def get_list_of_books(self):
        res = self.client.get(Books.BOOK_lIST)
        res.raise_for_status()
        return res.json()

    def add_book(self, isbns):
        res = self.client.post(Books.BOOK_lIST,
                                    json={"userId": self.user_id,
                                          "collectionOfIsbns": [{"isbn": isbn} for isbn in isbns]})
        res.raise_for_status()
        return res.json()

    def delete_book(self, isbn):
        res = self.client.delete(Books.BOOK,
                                 json={"userId": self.user_id,
                                       "isbn": isbn})
        res.raise_for_status()
        return res

    def delete_all_books(self, user_id):
        res = self.client.delete(f"{Books.BOOK_lIST}?UserId={user_id}")
        res.raise_for_status()
        return res

    def get_users_books(self, user_id):
        res = self.client.get(f"{User.USER_ACCOUNT}/{user_id}")
        res.raise_for_status()
        return res.json()
