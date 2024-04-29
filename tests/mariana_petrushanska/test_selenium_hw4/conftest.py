import pytest
from selenium.webdriver import Chrome
from tests.mariana_petrushanska.test_selenium_hw4 import constants
from tests.mariana_petrushanska.test_selenium_hw4 import LoginPage, ProductsPage


@pytest.fixture(scope="function")
def session():
    session = Chrome()
    yield session
    session.quit()


@pytest.fixture(autouse=True)
def login(session):
    login_page = LoginPage(session)
    login_page.open()
    login_page.fill_in_login_form(constants.LOGIN, constants.PASSWORD)
    login_page.confirm_login()


@pytest.fixture
@pytest.mark.usefixture("login")
def three_items_in_the_cart(session):
    products_page = ProductsPage(session)
    items = products_page.get_available_items()
    assert len(items) == 6

    products_page.add_to_cart(items[0])
    products_page.add_to_cart(items[3])
    products_page.add_to_cart(items[5])
