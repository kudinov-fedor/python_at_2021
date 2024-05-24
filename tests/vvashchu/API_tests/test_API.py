import pytest
from tests.vvashchu.API_tests.API_client import ApiClient
from tests.vvashchu.API_tests import constants as Const


@pytest.fixture
def session():
    user = ApiClient(Const.USER, Const.PASSWORD)
    yield user


def test_user_login(session: ApiClient):
    data = session.login_user()
    assert data["username"] == Const.USER


def test_get_profile(session: ApiClient):
    session.setup_user()
    profile = session.get_profile()
    assert profile.setdefault("username") == Const.USER


def test_get_book(session: ApiClient):
    session.setup_user()
    books = session.get_books()
    book1 = session.get_book(books["books"][1]["isbn"])
    assert book1.setdefault('isbn') == books["books"][1]["isbn"]


def test_get_books_count(session: ApiClient):
    session.setup_user()
    books = session.get_books()
    assert len(books["books"]) == 8


def test_change_book(session: ApiClient):
    session.setup_user()
    books = session.get_books()
    book1 = session.get_book(books["books"][1]["isbn"])
    isbn2 = books["books"][0]["isbn"]
    session.add_book(book1["isbn"])
    session.change_book(isbn=book1["isbn"], isbn2=isbn2)
    new_book = session.get_profile()["books"]
    assert len(new_book) == 1
    assert (new_book[0]["isbn"]) == isbn2


def test_delete_book(session: ApiClient):
    session.setup_user()
    books = session.get_books()
    book1 = session.get_book(books["books"][1]["isbn"])
    session.add_book(book1["isbn"])
    books_amount = session.get_profile()['books']

    session.delete_book(book1["isbn"])
    new_books_amount = session.get_profile()['books']

    assert len(new_books_amount) == (len(books_amount) - 1)
