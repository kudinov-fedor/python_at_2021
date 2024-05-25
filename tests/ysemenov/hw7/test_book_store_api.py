import pytest
from tests.ysemenov.hw7.api_client import ApiClient
from tests.ysemenov.hw7.constants import USERNAME, PASSWORD, ISBN, ISBN2


@pytest.fixture(scope="session")
def session():
    session = ApiClient(USERNAME, PASSWORD)
    session.create()
    yield session
    session.reset()


@pytest.fixture(autouse=True)
def remove_books(session: ApiClient):
    session.delete_books()


def test_get_books_count(session: ApiClient):
    books = session.get_books()["books"]
    assert len(books) == 8


def test_add_book_by_isbn(session: ApiClient):
    session.add_book(ISBN)
    assert len(session.get_user()["books"]) == 1
    session.add_book(ISBN2)
    assert len(session.get_user()["books"]) == 2


def test_add_books_from_list(session: ApiClient):
    books = session.get_books()["books"]
    session.add_book(books[0]["isbn"])
    assert len(session.get_user()["books"]) == 1
    session.add_book(books[1]["isbn"])
    assert len(session.get_user()["books"]) == 2


def test_add_all_books(session: ApiClient):
    books = session.get_books()["books"]
    initial_books_count = len(books)
    for book in books:
        session.add_book(book["isbn"])
    added_books_count = len(session.get_user()["books"])
    assert added_books_count == 8
    assert added_books_count == initial_books_count


def test_replace_book(session: ApiClient):
    session.add_book(ISBN)
    session.replace_book(ISBN, ISBN2)
    user_books = session.get_user()["books"]
    assert user_books[0]["isbn"] == ISBN2


def test_remove_book(session: ApiClient):
    books = session.get_books()["books"]
    session.add_book(books[0]["isbn"])
    session.delete_book(books[0]["isbn"])
    assert len(session.get_user()["books"]) == 0
