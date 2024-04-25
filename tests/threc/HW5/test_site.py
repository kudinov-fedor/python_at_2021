

from tests.threc.HW5.BasePage import BasePage
from tests.threc.HW5.LoginPage import LoginPage
from tests.threc.HW5.ProductPage import ProductPage
from tests.threc.HW5.CartPage import CartPage
import constants


def test_item_details(driver):
    base_page = BasePage(driver)
    base_page.open()
    login_page = LoginPage(base_page)
    login_page.login('standard_user', 'secret_sauce')
    product_page = ProductPage(driver)
    item_name = 'Sauce Labs Backpack'
    product_page.product_details()
    cart_page = CartPage(driver)
    # assert item_name == product_page.get_cart_item_name()


def test_product(driver):
    base_page = BasePage(driver)
    base_page.open()
    login_page = LoginPage(base_page)
    login_page.login('standard_user', 'secret_sauce')
    product_page = ProductPage(driver)
    product_page.add_to_cart()
    cart_page = CartPage(driver)
    assert cart_page.get_cart_badge_count() == '1'
