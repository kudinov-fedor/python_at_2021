import pytest
from tests.yana_pokulita.HW7_apiTests.Api_client import ApiClient
from tests.yana_pokulita.HW7_apiTests import Constants as Const


@pytest.fixture
def session():
    user = ApiClient(Const.USER, Const.PASSWORD)
    user.login_user()
    yield user


def test_user_login(session: ApiClient):
    data = session.login_user()
    assert data["username"] == Const.USER


def test_get_profile(session: ApiClient):
    profile = session.get_profile()
    assert profile.setdefault('userId') == Const.User_ID


def test_get_book(session: ApiClient):
    one_book = session.get_book(Const.ISBN_ID)
    assert one_book.setdefault('isbn') == Const.ISBN_ID


def test_get_books_count(session: ApiClient):
    books = session.get_books()
    assert len(books["books"]) == 8


def test_change_book(session: ApiClient):
    book = session.get_book(Const.ISBN_ID)
    session.add_books(book["isbn"])
    session.change_book(isbn=book["isbn"], isbn2=Const.NEW_ISBN)
    new_book = session.get_profile()["books"]

    assert len(new_book) == 1
    assert (new_book[0]["isbn"]) == Const.NEW_ISBN


def test_delete_book(session: ApiClient):
    session.add_books(Const.ISBN)
    books_amount = session.get_profile()['books']

    session.delete_book(Const.ISBN)
    new_books_amount = session.get_profile()['books']

    assert len(new_books_amount) == (len(books_amount) - 1)
