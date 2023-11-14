from tests.mizo.api_client import ApiClient
import pytest
from tests.mizo import constants


@pytest.fixture()
def api_client():
    api_client = ApiClient(constants.userName, constants.password)
    api_client.token = api_client.generate_token()["token"]
    api_client.user_id = api_client.user_login()["userId"]
    api_client.user_authorized()
    yield api_client


def test_add_books_to_collection(api_client):
    isbn_book_1 = api_client.get_all_books()["books"][0]["isbn"]
    isbn_book_2 = api_client.get_all_books()["books"][1]["isbn"]
    isbn_add_to_collection = isbn_book_1, isbn_book_2

    res = api_client.add_book_to_collection(isbn_add_to_collection)
    expected_res = {"books": [{"isbn": isbn} for isbn in isbn_add_to_collection]}
    assert res == expected_res


def test_delete_all_books(api_client):
    user_id = api_client.user_id
    api_client.delete_all_books(user_id)
    updated_books = api_client.user_books(user_id)
    assert len(updated_books['books']) == 0
