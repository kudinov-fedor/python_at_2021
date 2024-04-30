import pytest
from selenium.webdriver import Chrome
from tests.khrystynatk import pages
from tests.khrystynatk.pages.constants import *


@pytest.fixture
def driver():
    session = Chrome()
    session.implicitly_wait(0.5)
    yield session
    session.quit()


def test_landing_page(driver):
    """
    перевірити лендінг пейдж урлу
    """
    login_page = pages.LoginPage(driver).open_page(HOST)
    login_page.input_creds(USERNAME, PASSWORD)\
        .go_to_items_page()
    landing_page = pages.BasePage(driver)

    assert landing_page.get_url() == LANDING_PG


def test_elements(driver):
    """
    перевірити к-сть продуктів на сторінці
    """
    login_page = pages.LoginPage(driver).open_page(HOST)
    items_page = login_page.input_creds(USERNAME, PASSWORD)\
        .go_to_items_page()\
        .find_product_rows()

    assert len(items_page) == 6


def test_logout_user(driver):
    """
    перевірити логаут користувача
    """
    login_page = pages.LoginPage(driver).open_page(HOST)
    logout = login_page.input_creds(USERNAME, PASSWORD)\
        .go_to_items_page().logout_from_side_menu()

    assert logout.get_url() == LOGOUT_PG
    assert logout.find_username_field().is_displayed()
    assert logout.find_password_field().is_displayed()


def test_delete_all_from_cart(driver):
    """
    перевірити, що сторінка корзини пуста
    перевірити поточну урлу корзини
    """
    landing_page = pages.LoginPage(driver)
    landing_page.open_page(HOST)
    els = landing_page.input_creds(USERNAME, PASSWORD).go_to_items_page()
    els.add_to_cart(0)
    els.add_to_cart(1)
    els.add_to_cart(2)
    cart_page = els.go_to_cart()
    cart_page.remove_cart_item(0)
    cart_page.remove_cart_item(0)
    cart_page.remove_cart_item(0)
    current_page = pages.BasePage(driver)

    assert current_page.get_url() == CART_PG
    assert cart_page.get_cart_badge() == 0
