from requests.sessions import session
from tests.innahoncharenko.homework_7.config import AccountEndpoints
from tests.innahoncharenko.homework_7.config import BookStoreEndpoints


class BookStoreApi:

    def __init__(self, user, password):
        self.user_info = {
            "userName": user,
            "password": password,
        }
        self.user_id = None
        self.session = session()

    # Token
    @property
    def token(self):
        header = self.session.headers.get("Authorization")
        return header.replace("Bearer ", "") if header else None

    @token.setter
    def token(self, token):
        if token:
            self.session.headers["Authorization"] = f"Bearer {token}"
        else:
            del self.token

    @token.deleter
    def token(self):
        self.session.headers.pop("Authorization", None)

    # User
    def is_user_exist(self):
        response = self.session.post(AccountEndpoints.AUTHORIZED, self.user_info)
        return response.status_code == 200

    def get_user_info(self):
        response = self.session.get(f"{AccountEndpoints.USER}/{self.user_id}")
        response.raise_for_status()
        return response.json()

    def logout(self):
        self.token = None

    def login(self):
        if self.token:
            self.logout()

        result = self.session.post(AccountEndpoints.GENERATE_TOKEN, self.user_info)
        result.raise_for_status()
        self.token = result.json()["token"]
        return result.json()

    def create_user(self):
        response = self.session.post(AccountEndpoints.USER, self.user_info)
        if not response.ok:
            raise RuntimeError(f"Failed to create user, code {response.status_code} details: {response.text}")
        self.user_id = response.json()["userID"]

    def delete_user(self):
        self.login()
        result = self.session.delete(f"{AccountEndpoints.USER}/{self.user_id}")
        result.raise_for_status()

    # Books
    def get_books_list(self):
        result = self.session.get(BookStoreEndpoints.BOOKS)
        result.raise_for_status()
        return result.json()

    def get_book_info(self, isbn: str):
        result = self.session.get(f"{BookStoreEndpoints.BOOK}", params={
            "ISBN": isbn
        })
        result.raise_for_status()
        return result.json()

    def add_books(self, isbns):
        if not self.token:
            raise RuntimeError("Add books requires authorization")

        result = self.session.post(f"{BookStoreEndpoints.BOOKS}", json={
            "userID": self.user_id,
            "collectionOfIsbns": isbns
        })
        print(result)
        result.raise_for_status()
