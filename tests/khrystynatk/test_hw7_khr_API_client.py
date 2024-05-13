import pytest
from tests.khrystynatk.hw7_khr_API_client import ApiClient


@pytest.fixture(scope="session")
def user():
    new_user = ApiClient("KhrTest1", "Password1!")
    new_user.create_user()
    yield new_user
    new_user.reset_user()


def test_books_count(user: ApiClient):
    books = user.get_books()["books"]

    assert len(books) == 8
    assert books[0]["title"] == "Git Pocket Guide"


def test_get_book(user: ApiClient):
    book = user.get_some_book(get_books=user.get_books()["books"], index=3)
    assert book["title"] == "Speaking JavaScript"


def test_add_book(user: ApiClient):
    book = user.get_books()["books"][0]
    print(book["isbn"])
    user.add_some_book(book["isbn"])
    assert len(user.get_user()["books"]) == 1
