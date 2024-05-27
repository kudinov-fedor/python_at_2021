import pytest
from tests.yspryn.test_HW7_APItests import constants as Const
from tests.yspryn.test_HW7_APItests.API_client import ApiClient


@pytest.fixture()
def session():
    user = ApiClient(Const.USERNAME, Const.PASSWORD)
    user.setup_user(Const.USERNAME, Const.PASSWORD)
    user.remove_books()
    yield user


def test_books_count(session: ApiClient):
    books = session.get_books()
    assert len(books) == 8


def test_book_info(session: ApiClient):
    books = session.get_books()

    assert books[2]["title"] == "Designing Evolvable Web APIs with ASP.NET"
    assert books[2]["author"] == "Glenn Block et al."
    assert books[2]["pages"] == 238


def test_add_book(session: ApiClient):
    books = session.get_books()
    session.add_book(books[1]["isbn"])
    session.add_book(books[2]["isbn"])

    assert len(session.get_user()["books"]) == 2


def test_remove_book(session: ApiClient):
    books = session.get_books()
    session.add_book(books[1]["isbn"])
    session.add_book(books[2]["isbn"])

    assert len(session.get_user()["books"]) == 2

    session.remove_book(books[2]["isbn"])

    assert len(session.get_user()["books"]) == 1


def test_remove_all_books(session: ApiClient):
    books = session.get_books()
    session.add_book(books[1]["isbn"])
    session.add_book(books[2]["isbn"])

    assert len(session.get_user()["books"]) == 2

    session.remove_books()

    assert len(session.get_user()["books"]) == 0
