import pytest
from tests.mariana_petrushanska.test_api_hw7.constansts import User, Books


def test_user_login(client):
    user = client.user_login()
    assert user["username"] == User.USER_NAME


def test_number_of_books(client):
    list_of_books = client.get_list_of_books()
    assert len(list_of_books["books"]) == 8


def test_adding_books(client):
    book_1_isbn = client.get_list_of_books()["books"][1]["isbn"]
    book_2_isbn = client.get_list_of_books()["books"][4]["isbn"]
    book_3_isbn = client.get_list_of_books()["books"][7]["isbn"]
    books_to_add = book_1_isbn, book_2_isbn, book_3_isbn
    added_books = client.add_book(books_to_add)

    expected_result = {"books": [{"isbn": isbn} for isbn in books_to_add]}
    assert added_books == expected_result


def test_delete_one_book(client):
    user_id = client.user_id

    book_1_isbn = client.get_list_of_books()["books"][1]["isbn"]
    book_2_isbn = client.get_list_of_books()["books"][4]["isbn"]
    book_3_isbn = client.get_list_of_books()["books"][7]["isbn"]
    books_to_add = book_1_isbn, book_2_isbn, book_3_isbn
    client.add_book(books_to_add)

    added_books_amount = client.get_users_books(user_id)["books"]

    client.delete_book(Books.BOOK_ISBN)
    updated_books_amount = client.get_users_books(user_id)["books"]

    assert len(updated_books_amount) == (len(added_books_amount) - 1)


def test_delete_all_books(client):
    user_id = client.user_id

    book_1_isbn = client.get_list_of_books()["books"][1]["isbn"]
    book_2_isbn = client.get_list_of_books()["books"][4]["isbn"]
    book_3_isbn = client.get_list_of_books()["books"][7]["isbn"]
    books_to_add = book_1_isbn, book_2_isbn, book_3_isbn
    client.add_book(books_to_add)

    client.delete_all_books(user_id)
    updated_books_amount = client.get_users_books(user_id)["books"]

    assert len(updated_books_amount) == 0
