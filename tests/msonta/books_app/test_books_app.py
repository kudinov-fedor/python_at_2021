from tests.msonta.books_app.books_app_page import LoginPage, BookPage, ProfilePage
from selenium.webdriver.remote.webdriver import WebDriver
from tests.msonta.books_app import config
import pytest


# view books
def test_search_books(driver: WebDriver):
    search_text = "JavaScript "
    book_page = BookPage(driver)
    book_page.open()
    assert book_page.get_books_count(book_page.BOOKS) == 8
    book_page.search(value=search_text)
    assert book_page.get_books_count(book_page.BOOKS) == 2


# login
def test_login(driver: WebDriver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(user_name=config.USER, password=config.PASSWORD)
    assert driver.current_url == login_page.host + "/profile"


# add book
def test_add_book(login: WebDriver):
    books = ["Git Pocket Guide", "Speaking JavaScript"]
    book_page = BookPage(login)
    book_page.navigate_to_page(book_page.MENU_LINK)

    for book in books:
        book_page.scroll_down()
        book_page.add_book_to_collection(book)
        alert = book_page.get_alert()
        assert alert.text == "Book added to your collection."
        book_page.accept_alert(alert)
        book_page.get_element(*book_page.GO_BACK).click()


# view own books
def test_view_own_books(login: WebDriver):
    profile_page = ProfilePage(login)
    profile_page.scroll_up()
    own_books = profile_page.get_books_count(profile_page.BOOKS_TABLE_ITEM)
    assert own_books == 2


@pytest.mark.dependency(depends=["test_add_book"])
def test_delete_book(login: WebDriver):
    book_to_delete = "Git Pocket Guide"
    profile_page = ProfilePage(login)
    profile_page.delete_book(book_to_delete)
    alert = profile_page.get_alert()
    assert alert.text == "Book deleted."
    alert.accept()
    assert profile_page.get_books_count(profile_page.BOOKS_TABLE_ITEM) == 1


@pytest.mark.dependency(depends=["test_delete_book"])
def test_delete_all_books(login: WebDriver):
    profile_page = ProfilePage(login)
    profile_page.navigate_to_page(profile_page.MENU_LINK)
    profile_page.delete_all_books()
    alert = profile_page.get_alert()
    assert alert.text == "All Books deleted."
    alert.accept()
    assert profile_page.get_books_count(profile_page.BOOKS_TABLE_ITEM) == 0
