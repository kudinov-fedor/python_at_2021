import pytest
from requests.exceptions import HTTPError
from tests.innahoncharenko.homework_7.config import Constants
from tests.innahoncharenko.homework_7.BookStoreApi import BookStoreApi


@pytest.fixture
def client():
    client = BookStoreApi(Constants.USER_NAME, Constants.USER_PASS)

    if not client.is_user_exist():
        client.create_user()

    yield client

    if client.is_user_exist():
        client.delete_user()


# account test
def test_user_should_exist(client):
    assert client.is_user_exist()


def test_user_is_deleted(client):
    client.delete_user()
    assert not client.is_user_exist()


def test_get_user_info_requires_auth(client):
    with pytest.raises(HTTPError):
        client.get_user_info()


def test_user_name_in_user_info(client):
    client.login()
    user_info = client.get_user_info()
    assert user_info["username"] == Constants.USER_NAME


# Books tests
def test_get_books_info(client):
    books_list = client.get_books_list()
    assert "books" in books_list.keys()


def test_get_book_info(client):
    books_list = client.get_books_list()
    book_isbn = books_list["books"][0]["isbn"]
    book_info = client.get_book_info(book_isbn)
    assert book_isbn == book_info["isbn"]


def test_add_books_requires_auth(client):
    books_list = client.get_books_list()
    book_isbn = books_list["books"][0]["isbn"]
    with pytest.raises(RuntimeError):
        client.add_books([book_isbn])


def test_add_books(client):
    books_list = client.get_books_list()
    book_isbn = books_list["books"][0]["isbn"]
    client.login()
    client.add_books([book_isbn])
    user_info = client.get_user_info()
    assert book_isbn == user_info["books"][0]["isbn"]
