from locust import HttpUser, between, task

from tests.mizo.apiClient_for_locust import LocustApiClient
from tests.mizo.generate_user_names_and_set_test_password import generate_next_username
from tests.mizo.generate_user_names_and_set_test_password import set_test_password


class AuthClient(HttpUser, LocustApiClient):
    wait_time = between(1, 5)

    def on_start(self):
        self.login = generate_next_username()
        self.password = set_test_password()
        response = self.user_create()
        self.user_id = response.get("userID")
        self.login = response.get("username")

        # GET TOKEN
        response = self.generate_token()
        authorization_token = response.get("token")

        # SET TOKEN:
        self.client.headers["Authorization"] = "Bearer " + authorization_token

    @task
    def perform_user_login(self):
        self.user_login()

    @task
    def perform_user_authorized(self):
        self.user_authorized()

    @task
    def perform_get_all_books(self):
        self.get_all_books()

    @task
    def perform_add_book_to_collection_and_remove(self):
        # remove all books
        self.delete_all_books(self.user_id)

        # get all books
        response = self.get_all_books()
        isbns = [book.get("isbn") for book in response.get("books")]

        # add first two books
        self.add_book_to_collection(isbns[:2])

        # delete specific book
        isbn_to_delete = isbns[0]
        self.delete_book(isbn_to_delete)
