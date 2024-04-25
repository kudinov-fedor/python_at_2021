import pytest
from selenium.webdriver import Chrome
from selenium.common import NoSuchElementException
from tests.khrystynatk.hw5_khr_Page_object import LoginPage
from tests.khrystynatk.hw5_khr_Page_object import ItemsPage
from tests.khrystynatk.hw5_khr_Page_object import CartPage
from tests.khrystynatk.hw5_khr_Page_object.constants import *
from tests.khrystynatk.hw5_khr_Page_object.locators1 import LoginPageLoc


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
    login_page.open_login_page()
    login_page.provide_creds()
    current_page = driver.current_url
    assert current_page == LANDING_PG


def test_elements(driver):
    """
    перевірити к-сть продуктів на сторінці
    """
    landing_page = ItemsPage(driver)
    landing_page.open_landing_page()
    elements = landing_page.find_elements()
    assert len(elements) == 6


def test_logout_user(driver):
    """
    перевірити логаут користувача
    """
    landing_page = ItemsPage(driver)
    landing_page.open_landing_page()
    landing_page.logout_from_side_menu()

    assert driver.current_url == LOGOUT_PG
    assert driver.find_element(*LoginPageLoc.TXT_USERNAME).is_displayed()
    assert driver.find_element(*LoginPageLoc.TXT_PASSWORD).is_displayed()


def test_delete_all_from_cart(driver):
    """
    перевірити, що сторінка корзини пуста
    перевірити поточну урлу корзини
    """
    cart_page = CartPage(driver)
    cart_page.open_landing_page()
    cart_page.add_items()
    cart_page.move_to_cart()
    cart_page.remove_cart_items()

    assert driver.current_url == CART_PG
    with pytest.raises(NoSuchElementException):
        cart_page.cart_container()
