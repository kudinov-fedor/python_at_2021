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
# (autouse=True)
def login(session):

    LoginPage(session).open().fill_form(constants.LOGIN, constants.PASSWORD)


@pytest.fixture
# @pytest.mark.usefixtures("login")
def cart_with_2_items(session, login):

    # elements_page = page.ProductsPage(session)
    # assert len(elements_page.get_products()) == 6
    #
    # # elements_page.move_product_to_cart(0)
    # # elements_page.move_product_to_cart(3)

    elements_page = page.ProductsPage(session)
    products = elements_page.get_products()
    assert len(products) == 6

    products[0].add_to_cart()
    products[3].add_to_cart()
