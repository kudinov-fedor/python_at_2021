import pytest
from tests.yspryn.HW2.locators import *
from selenium.webdriver import Chrome


HOST = "https://www.saucedemo.com"
LOGIN = "standard_user"
PASSWORD = "secret_sauce"


@pytest.fixture(scope="function")
def session():
    my_session = Chrome()
    yield my_session

    # tear down
    my_session.quit()


@pytest.fixture(autouse=True)
def user_login(session):
    session.get(HOST)
    session.find_element(*TXT_LOGIN_INPUT).send_keys(LOGIN)
    session.find_element(*TXT_PASSWORD_INPUT).send_keys(PASSWORD)
    session.find_element(*BTN_SUBMIT).click()


@pytest.fixture()
def add_products_to_cart(session):
    elements = session.find_elements(*TABLE_PRODUCT_ITEMS)
    elements[0].find_element(*BTN_ADD_TO_CART).click()
    elements[2].find_element(*BTN_ADD_TO_CART).click()
