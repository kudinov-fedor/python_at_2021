import pytest

from tests.threc.hw_api_demoqa.api_client import ApiClient
from tests.threc.hw_api_demoqa.constants import Site


@pytest.fixture(autouse=True)
def client():
    user = ApiClient(Site.USER, Site.PASSWORD)
    user.user_login()
    yield user
    user.delete_books()


def test_user_login(client: ApiClient):
    data = client.user_login()
    assert data["username"] == Site.USER


def test_get_book(client: ApiClient):
    one_book = client.get_book(Site.ISBN_ID)
    assert one_book.setdefault('isbn') == Site.ISBN_ID


def test_get_books(client: ApiClient):
    books = client.get_books()
    assert len(books["books"]) == 8


def test_get_profile(client: ApiClient):
    profile = client.get_profile()
    assert profile.setdefault('userId') == Site.USER_ID


def test_add_book(client: ApiClient):
    user = client.get_profile()
    amount = len(user['books'])

    client.add_books(Site.NEW_ISBN)
    user = client.get_profile()
    new_amount = len(user['books'])

    assert Site.NEW_ISBN == user['books'][-1]['isbn']

    assert new_amount == (amount + 1)


def test_delete_book(client: ApiClient):
    client.add_books(Site.ISBN)
    books_amount = client.get_profile()['books']

    client.delete_book(Site.ISBN)
    new_books_amount = client.get_profile()['books']

    assert len(new_books_amount) == (len(books_amount) - 1)
