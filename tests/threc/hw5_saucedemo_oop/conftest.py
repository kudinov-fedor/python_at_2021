import pytest
from selenium.webdriver import Chrome
from tests.threc.hw5_saucedemo_oop.page_object.login_page import LoginPage as LP
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
    login_page = LP(driver)
    login_page.open()
    login_page.fill_form(constants.LOGIN, constants.PASSWORD)
    login_page.submit()
