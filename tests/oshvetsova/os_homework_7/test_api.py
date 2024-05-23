import pytest
from .api_client import ApiClient
from .constant import USERNAME, PASSWORD, OLD_ISBN, NEW_ISBN


@pytest.fixture(autouse=True)
def client():
    user = ApiClient(USERNAME, PASSWORD)
    user.create()
    yield user
    user.reset()


def test_user_login(client: ApiClient):
    assert client.user_login()["username"] == USERNAME


def test_get_books(client: ApiClient):
    assert len(client.books_get()["books"]) == 8


def test_add_book(client: ApiClient):
    client.books_add(OLD_ISBN)
    assert len(client.user_get()["books"]) == 1


def test_delete_book(client: ApiClient):
    client.books_add(NEW_ISBN)
    new_books_list = client.user_get()['books']
    client.books_delete(NEW_ISBN)
    new_books_amount = client.user_get()['books']
    assert len(new_books_amount) == (len(new_books_list) - 1)
