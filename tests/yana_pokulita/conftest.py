import pytest
from selenium.webdriver import Chrome
from tests.yana_pokulita.HW4_DemoQA import page
from tests.yana_pokulita.HW4_DemoQA.page import constants


@pytest.fixture
def session():
    session = Chrome()
    yield session
    session.quit()


@pytest.fixture(autouse=True)
def login(session):

    login_page = page.LoginPage(session)
    login_page.open()
    login_page.fill_form(constants.LOGIN, constants.PASSWORD)


@pytest.fixture
@pytest.mark.usefixtures("login")
def cart_with_2_items(session):

    elements_page = page.ProductsPage(session)
    assert len(elements_page.get_products()) == 6

    elements_page.move_product_to_cart(0)
    elements_page.move_product_to_cart(3)



