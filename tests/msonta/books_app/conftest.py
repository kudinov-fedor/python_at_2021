import pytest
from selenium.webdriver import Chrome, ChromeOptions
from tests.msonta.books_app.books_app_page import LoginPage, BookPage
from tests.msonta.books_app import config


@pytest.fixture()
def driver():
    options = ChromeOptions()
    driver = Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.stop_client()
    driver.quit()


# TODO
@pytest.fixture()
def login(driver):
    """
    Get initialized driver for this test and login to the application,
    returning the driver instance. Logout silently after the test.
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(config.USER, config.PASSWORD)

    yield driver
    login_page.logout()


@pytest.fixture()
def add_book_to_profile(login, books: []):
    for book in books:
        book_page = BookPage(login)
        book_page.navigate_to_page(book_page.MENU_LINK)
        book_page.add_book_to_collection(book)
        alert = book_page.get_alert()
        book_page.accept_alert(alert)
