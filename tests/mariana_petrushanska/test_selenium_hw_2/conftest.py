import pytest
from selenium.webdriver import Chrome
from tests.mariana_petrushanska.test_selenium_hw_2 import constants
from tests.mariana_petrushanska.test_selenium_hw_2.locators import LoginPage
from tests.mariana_petrushanska.test_selenium_hw_2.locators import ProductsPage


@pytest.fixture(scope="function", autouse=True)
def session():
    session = Chrome()
    yield session
    session.quit()


@pytest.fixture(autouse=True)
def login(session):
    session.get(constants.HOST)

    session.find_element(*LoginPage.TXT_USERNAME).send_keys(constants.LOGIN)
    session.find_element(*LoginPage.TXT_PASSWORD).send_keys(constants.PASSWORD)
    session.find_element(*LoginPage.BTN_LOGIN).click()


@pytest.fixture
@pytest.mark.usefixture("login")
def three_items_in_the_cart(session):
    element = session.find_elements(*ProductsPage.LST_ITEMS)
    assert len(element) == 6

    element[0].find_element(*ProductsPage.BTN_ADD_TO_CART).click()
    element[3].find_element(*ProductsPage.BTN_ADD_TO_CART).click()
    element[5].find_element(*ProductsPage.BTN_ADD_TO_CART).click()
