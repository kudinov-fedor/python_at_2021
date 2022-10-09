import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from tests.dnazar import context
from tests.dnazar import constants


# put your login, password here
USER = ""
PASSWORD = ""


@pytest.fixture
def login(session):
    login_context = context.LoginPageContext(session)
    login_context \
        .open_page(constants.LOGIN_PAGE_LINK) \
        .fill_user_name_field(USER) \
        .fill_password_field(PASSWORD) \
        .click_login_button()
    yield session
    login_context.click_logout_button()


def test_search(session: WebDriver):
    search_text = "JavaScript "
    all_books_count, expected_cont = 8, 2
    books_context = context.BookBasePageContext(session)
    books_context.open_page(constants.BOOKS_PAGE_LINK) \
        .verify_books_count(all_books_count) \
        .fill_search_field(search_text) \
        .verify_books_count(expected_cont) \
        .clear_search_field()


def test_adding_books(login: WebDriver):
    books = ["Git Pocket Guide", "Learning JavaScript Design Patterns"]
    book_added_text = "Book added to your collection."
    expected_count = 2
    books_context = context.BookBasePageContext(login)
    for book in books:
        books_context \
            .open_page(constants.BOOKS_PAGE_LINK) \
            .click_book_title_link(book) \
            .click_add_to_collection_button() \
            .verify_alert_text(books_context.switch_to_alert(7), book_added_text) \
            .accept_alert(books_context.switch_to_alert(3))
    context.ProfilePageContext(login) \
        .open_page(constants.PROFILE_PAGE_LINK) \
        .verify_books_count(expected_count)


@pytest.mark.dependency(depends=["test_adding_books"])
def test_deleting_books(login: WebDriver):
    expected_count = 1
    book, books_deleted_text = "Git Pocket Guide", "All Books deleted."
    profile_context = context.ProfilePageContext(login)
    profile_context \
        .click_book_delete_item(book) \
        .click_ok_button_modal_window() \
        .accept_alert(profile_context.switch_to_alert(3)) \
        .verify_books_count(expected_count) \
        .click_delete_all_books_button() \
        .click_ok_button_modal_window() \
        .verify_alert_text(profile_context.switch_to_alert(6), books_deleted_text) \
        .accept_alert(profile_context.switch_to_alert(3))


@pytest.mark.dependency(depends=["test_deleting_books"])
def test_profile_books(login: WebDriver):
    expected_count = 0
    context.ProfilePageContext(login) \
        .verify_books_count(expected_count)
