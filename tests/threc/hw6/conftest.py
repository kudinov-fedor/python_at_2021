import pytest
from selenium.webdriver import Chrome
from tests.threc.hw6.page_object.login_page import LoginPage
import constants


@pytest.fixture()
def driver():
    driver = Chrome()
    yield driver

    # tear down
    driver.quit()


@pytest.fixture(autouse=True)
def login(driver):
    """
    Log in to the site
    """
    LoginPage(driver)   \
        .open() \
        .fill_form(constants.LOGIN, constants.PASSWORD) \
        .submit_login_form()
