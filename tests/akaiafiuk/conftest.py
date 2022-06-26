import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.remote.webdriver import WebDriver

from tests.akaiafiuk.book_store_ui.pages.login_page import LoginPage
from tests.akaiafiuk.constants import LOGIN, PASSWORD


@pytest.fixture()
def test_list():
    return [1, 2, 3]


@pytest.fixture(scope='session')
def session() -> WebDriver:
    driver = Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def prepared_user(session) -> WebDriver:
    session.delete_all_cookies()
    session.refresh()
    LoginPage(session).open().login(LOGIN, PASSWORD)
    yield session
    session.delete_all_cookies()
    session.refresh()
