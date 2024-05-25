from locust import HttpUser, between, task
from tests.mizo.generate_user_names import generate_next_username
from tests.mizo.constants import PASSWORD


class AuthClient(HttpUser):
    wait_time = between(1, 5)
    userID = None
    user_name = None
    password = None

    def on_start(self):
        next_user_name = generate_next_username()
        self.user_name = next_user_name
        self.password = PASSWORD
        response = self.client.post(self.host + "/Account/v1/user",
                                    json={"userName": self.user_name,
                                          "password": self.password})
        self.userID = response.json().get("userID")
        self.user_name = response.json().get("username")

        # GET TOKEN
        response = self.client.post(self.host + "/Account/v1/GenerateToken",
                                    json={"userName": self.user_name,
                                          "password": self.password})
        authorization_token = response.json().get("token")

        # SET TOKEN:
        self.client.headers["Authorization"] = "Bearer " + authorization_token

    @task
    def user_login(self):
        response = self.client.post(self.host + "/Account/v1/Login",
                                    json={"userName": self.user_name,
                                          "password": self.password})

    @task
    def user_authorized(self):
        self.client.post(self.host + "/Account/v1/Authorized",
                         json={"userName": self.user_name,
                               "password": self.password})

    @task
    def get_all_books(self):
        self.client.get(self.host + "/BookStore/v1/Books")

    @task
    def add_book_to_collection_and_remove(self):
        # remove all books
        self.client.delete(self.host + "/BookStore/v1/Books/?UserId=" + self.userID)

        # get all books
        response = self.client.get(self.host + "/BookStore/v1/Books")
        isbns = [book.get("isbn") for book in response.json().get("books")]

        # add first two books
        self.client.post(self.host + "/BookStore/v1/Books",
                         json={"userId": self.userID,
                               "collectionOfIsbns": [{"isbn": isbn} for isbn in isbns[:2]]})

        # delete specific book
        isbn_to_delete = isbns[0]
        self.client.delete(self.host + "/BookStore/v1/Book",
                           json={"isbn": isbn_to_delete,
                                 "userId": self.userID})
