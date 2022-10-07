from tests.msonta.books_app.books_app_page import LoginPage, BookPage, ProfilePage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.msonta.books_app import config
import pytest

timeout = 5


# view books
def test_search_books(driver: WebDriver):
    search_text = "JavaScript "
    book_page = BookPage(driver)
    book_page.open()

    WebDriverWait(driver, timeout)\
        .until(EC.url_contains(book_page.url))

    assert book_page.get_books_count(book_page.books_locators) == 8

    book_page.search(value=search_text)
    assert book_page.get_books_count(book_page.books_locators) == 2


# login
def test_login(driver: WebDriver):
    login_page = LoginPage(driver)
    login_page.open()

    WebDriverWait(driver, timeout)\
        .until(EC.url_contains(login_page.url))

    login_page.login(user_name=config.USER, password=config.PASSWORD)

    WebDriverWait(driver, timeout)\
        .until(EC.url_contains(login_page.host + "/profile"))

    assert driver.current_url == login_page.host + "/profile"


# add book
def test_add_book(login: WebDriver):
    go_back_button = (By.CSS_SELECTOR, ".text-left #addNewRecordButton")
    books = ["Git Pocket Guide", "Speaking JavaScript"]

    book_page = BookPage(login)
    book_page.navigate_to_page(book_page.book_store_menu_item)

    for book in books:
        book_page.scroll_down()
        book_page.add_book_to_collection(book)

        alert = book_page.get_alert()
        assert alert.text == "Book added to your collection."
        book_page.accept_alert(alert)
        book_page.get_element(*go_back_button).click()


# view own books
def test_view_own_books(login: WebDriver):
    profile_page = ProfilePage(login)
    profile_page.navigate_to_page(profile_page.profile_menu_item)
    own_books = profile_page.get_books_count(profile_page.books_locators)

    assert own_books == 2


@pytest.mark.dependency(depends=["test_add_book"])
def test_delete_book(login: WebDriver):
    book_to_delete = "Git Pocket Guide"
    profile_page = ProfilePage(login)
    profile_page.delete_book(book_to_delete)

    alert = profile_page.get_alert()
    assert alert.text == "Book deleted."
    alert.accept()

    assert profile_page.get_books_count(profile_page.books_locators) == 1


@pytest.mark.dependency(depends=["test_delete_book"])
def test_delete_all_books(login: WebDriver):
    profile_page = ProfilePage(login)
    profile_page.navigate_to_page(profile_page.profile_menu_item)
    profile_page.delete_all_books()
    alert = profile_page.get_alert()
    assert alert.text == "All Books deleted."
    alert.accept()

    assert profile_page.get_books_count(profile_page.books_locators) == 0
