import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from tests.dnazar import context
from tests.dnazar import constants


# put your login, password here
USER = ""
PASSWORD = ""


def login(driver: WebDriver):
    login_context = context.LoginPageContext(driver)
    login_context.open_page(constants.LOGIN_PAGE_LINK) \
        .fill_user_name_field(USER) \
        .fill_password_field(PASSWORD) \
        .click_login_button()\
        .verify_logout_button_enabled()


def test_search(session: WebDriver):
    search_text = "JavaScript "
    all_books_count, expected_cont = 8, 2
    books_context = context.BookBasePageContext(session)
    books_context.open_page(constants.BOOKS_PAGE_LINK) \
        .verify_books_count(all_books_count) \
        .fill_search_field(search_text) \
        .verify_books_count(expected_cont) \
        .clear_search_field()


def test_adding_books(session: WebDriver):
    books = ["Git Pocket Guide", "Learning JavaScript Design Patterns"]
    book_added_text = "Book added to your collection."
    expected_count = 2
    login(session)
    books_context = context.BookBasePageContext(session)
    for book in books:
        books_context.open_page(constants.BOOKS_PAGE_LINK) \
            .click_book_title_link(book) \
            .click_add_to_collection_button() \
            .switch_to_alert() \
            .verify_alert_text(book_added_text) \
            .accept_alert() \
            .click_back_to_store_button()
    profile_context = context.ProfilePageContext(session)
    profile_context.open_page(constants.PROFILE_PAGE_LINK)\
        .verify_books_count(expected_count)


@pytest.mark.dependency(depends=["test_adding_books"])
def test_deleting_books(session: WebDriver):
    expected_count = 1
    book, books_deleted_text = "Git Pocket Guide", "All Books deleted."
    login(session)
    profile_context = context.ProfilePageContext(session)
    profile_context \
        .click_book_delete_item(book) \
        .click_ok_button_modal_window() \
        .switch_to_alert() \
        .accept_alert() \
        .verify_books_count(expected_count) \
        .click_delete_all_books_button() \
        .click_ok_button_modal_window() \
        .switch_to_alert() \
        .verify_alert_text(books_deleted_text) \
        .accept_alert() \
        .click_logout_button()


@pytest.mark.dependency(depends=["test_deleting_books"])
def test_profile_books(session: WebDriver):
    expected_cont = 0
    login(session)
    profile_context = context.ProfilePageContext(session)
    profile_context \
        .verify_books_count(expected_cont)
