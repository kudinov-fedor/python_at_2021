from requests import session
from tests.mariana_petrushanska.test_api_hw7.constansts import General, User, Books


class ApiClient:

    def __init__(self, login: str, password: str):
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

    def get_user_info(self):
        self.token = self.generate_token()["token"]
        self.user_id = self.user_login()["userId"]
        self.user_authorized()

    def user_exists(self):
        """
        Checks whether it is possible to create new user:
        1. if possible -> user is automatically created
        2. if it is not possible to create a user -> 406. "User exists!" error is shown
        (which is a marker for this method that user already exists).
        """
        res = self.client.post(User.USER_ACCOUNT,
                               json={"userName": self.login,
                                     "password": self.password})
        return res.status_code == 406

    def create_user(self):
        res = self.client.post(User.USER_ACCOUNT,
                               json={"userName": self.login,
                                     "password": self.password})
        res.raise_for_status()
        return res.json()

    def delete_user(self):
        res = self.client.delete(f"{User.USER_ACCOUNT}/{self.user_id}")
        return res.status_code == 204

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
        res = self.client.get(Books.BOOK_LIST)
        res.raise_for_status()
        return res.json()

    def add_book(self, isbns):
        res = self.client.post(Books.BOOK_LIST,
                               json={"userId": self.user_id,
                                     "collectionOfIsbns": [{"isbn": isbn} for isbn in isbns]})
        res.raise_for_status()
        return res.json()

    def delete_book(self, isbn: str):
        res = self.client.delete(Books.BOOK,
                                 json={"userId": self.user_id,
                                       "isbn": isbn})
        res.raise_for_status()
        return res

    def delete_all_books(self, user_id: str):
        res = self.client.delete(f"{Books.BOOK_LIST}?UserId={user_id}")
        res.raise_for_status()
        return res

    def get_users_books(self, user_id: str):
        res = self.client.get(f"{User.USER_ACCOUNT}/{user_id}")
        res.raise_for_status()
        return res.json()
