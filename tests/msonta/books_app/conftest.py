import pytest
from selenium.webdriver import Chrome, ChromeOptions
from tests.msonta.books_app.books_app_page import LoginPage
from tests.msonta.books_app import config


@pytest.fixture()
def driver():
    options = ChromeOptions()
    driver = Chrome(options=options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.stop_client()
    driver.quit()


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
