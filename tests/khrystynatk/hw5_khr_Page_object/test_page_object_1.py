import pytest
from selenium.webdriver import Chrome
from selenium.common import NoSuchElementException
from tests.khrystynatk.hw5_khr_Page_object import LoginPage
from tests.khrystynatk.hw5_khr_Page_object import ItemsPage
from tests.khrystynatk.hw5_khr_Page_object import CartPage
from tests.khrystynatk.hw5_khr_Page_object.base_page import BasePage
from tests.khrystynatk.hw5_khr_Page_object.constants import *


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
    login_page = LoginPage(driver)
    login_page.open_login_page(HOST)
    login_page.input_creds(USERNAME, PASSWORD)
    current_page_url = BasePage(driver)

    assert current_page_url.get_url() == LANDING_PG


def test_elements(driver):
    """
    перевірити к-сть продуктів на сторінці
    """
    landing_page = LoginPage(driver)
    landing_page.open_login_page(HOST)
    landing_page.input_creds(USERNAME, PASSWORD)
    elements_page = ItemsPage(driver)
    elements_page.find_elements()

    assert len(elements_page.find_elements()) == 6


def test_logout_user(driver):
    """
    перевірити логаут користувача
    """
    landing_page = LoginPage(driver)
    landing_page.open_login_page(HOST)
    landing_page.input_creds(USERNAME, PASSWORD)
    side_menu = ItemsPage(driver)
    side_menu.logout_from_side_menu()
    current_page_url = BasePage(driver)

    assert current_page_url.get_url() == LOGOUT_PG
    assert current_page_url.find_username_field().is_displayed()
    assert current_page_url.find_password_field().is_displayed()


def test_delete_all_from_cart(driver):
    """
    перевірити, що сторінка корзини пуста
    перевірити поточну урлу корзини
    """
    landing_page = LoginPage(driver)
    landing_page.open_login_page(HOST)
    landing_page.input_creds(USERNAME, PASSWORD)
    landing_page = ItemsPage(driver)
    landing_page.add_to_cart(0)
    landing_page.add_to_cart(1)
    landing_page.add_to_cart(2)
    landing_page.move_to_cart()
    cart_page = CartPage(driver)
    cart_page.remove_cart_items(0)
    cart_page.remove_cart_items(0)
    cart_page.remove_cart_items(0)
    current_page_url = BasePage(driver)

    assert current_page_url.get_url() == CART_PG
    with pytest.raises(NoSuchElementException):
        cart_page.get_cart_badge()
