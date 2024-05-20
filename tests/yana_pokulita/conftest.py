import pytest
from selenium.webdriver import Chrome
from tests.yana_pokulita.HW4_DemoQA import page
from tests.yana_pokulita.HW4_DemoQA.page.login_page import LoginPage
from tests.yana_pokulita.HW4_DemoQA.page import constants


@pytest.fixture
def session():
    session = Chrome()
    yield session
    session.quit()


@pytest.fixture
def login(session):

    LoginPage(session).open().fill_form(constants.LOGIN, constants.PASSWORD)


@pytest.fixture
def cart_with_2_items(session, login):

    elements_page = page.ProductsPage(session)
    products = elements_page.get_products()
    assert len(products) == 6

    products[0].add_to_cart()
    products[3].add_to_cart()
