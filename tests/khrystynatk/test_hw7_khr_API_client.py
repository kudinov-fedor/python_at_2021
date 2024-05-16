import pytest
from tests.khrystynatk.hw7_khr_API_client import ApiClient
from tests.khrystynatk import hw7_khr_Constants as Const


@pytest.fixture(scope="session")
def user():
    new_user = ApiClient(Const.USERNAME, Const.PASSWORD)
    new_user.create_user()
    yield new_user
    new_user.reset_user()


@pytest.fixture(autouse=True)
@pytest.mark.usefixtures("user")
def delete_all_books(user):
    user.delete_books()


def test_books_count(user: ApiClient):
    books = user.get_books()

    assert len(books) == 8
    assert books[3]["title"] == Const.BOOK_TITLE


def test_get_book(user: ApiClient):
    books = user.get_books()
    book = user.get_book(books[3]["isbn"])

    assert book["isbn"] == Const.ISBN
    assert book["title"] == Const.BOOK_TITLE


def test_add_book(user: ApiClient):
    book = user.get_books()[0]
    user.add_book(book["isbn"])

    assert len(user.get_user()["books"]) == 1


def test_change_book(user: ApiClient):
    book = user.get_books()[1]
    user.add_book(book["isbn"])
    user.change_book(isbn=book["isbn"], isbn2=Const.NEW_ISBN)
    new_book = user.get_user()["books"]

    assert len(new_book) == 1
    assert (new_book[0]["isbn"]) == Const.NEW_ISBN


def test_delete_book(user: ApiClient):
    book = user.get_books()[1]
    user.add_book(book["isbn"])
    user.delete_book(isbn=book["isbn"])
    assert len(user.get_user()["books"]) == 0
