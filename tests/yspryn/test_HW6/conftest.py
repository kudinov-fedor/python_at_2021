import pytest
from selenium.webdriver import Chrome
from tests.yspryn.test_HW6 import pages

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
    login_page.fill_login_form(LOGIN, PASSWORD).submit_form()


@pytest.fixture()
def add_products_to_cart(session):
    catalog_page = pages.CatalogPage(session).list_of_products_to_buy()
    catalog_page[0].add_item_to_cart()
    catalog_page[3].add_item_to_cart()
