import pytest
from selenium.webdriver import Chrome
from tests.yspryn.test_HW5 import pages

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
    login_page = pages.LoginPage(session)
    login_page.open_page()
    login_page.fill_login_form(LOGIN, PASSWORD)


@pytest.fixture()
def add_products_to_cart(session):
    catalog_page = pages.CatalogPage(session)
    catalog_page.add_product_to_cart(0)
    catalog_page.add_product_to_cart(2)
