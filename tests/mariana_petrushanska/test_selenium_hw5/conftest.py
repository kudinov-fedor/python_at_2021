import pytest
from selenium.webdriver import Chrome
from tests.mariana_petrushanska.test_selenium_hw5 import constants
from tests.mariana_petrushanska.test_selenium_hw5 import LoginPage, ProductsPage


@pytest.fixture(scope="function")
def session():
    session = Chrome()
    yield session
    session.quit()


@pytest.fixture(autouse=True)
def login(session):
    login_page = LoginPage(session)
    product_page = login_page.open() \
        .fill_in_login_form(constants.LOGIN, constants.PASSWORD) \
        .confirm_login()
    return product_page


@pytest.fixture
@pytest.mark.usefixture("login")
def three_items_in_the_cart(session):

    products_page = ProductsPage(session)
    items = products_page.available_items
    assert len(items) == 6

    items[0].add_to_cart()
    items[3].add_to_cart()
    items[5].add_to_cart()

