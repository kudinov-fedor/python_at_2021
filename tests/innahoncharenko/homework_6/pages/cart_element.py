from tests.innahoncharenko.homework_6.pages.locators import CartLocators
from selenium.common import NoSuchElementException


class CartElement:
    def __init__(self, web_driver):
        self.driver = web_driver

    def open_cart_page(self):
        self.driver.find_element(*CartLocators.CART).click()
        from tests.innahoncharenko.homework_6.pages.cart_page import CartPage
        return CartPage(self.driver)

    @property
    def get_items_in_cart_number(self):
        cart = self.driver.find_element(*CartLocators.CART)
        try:
            cart_badge = cart.find_element(*CartLocators.CART_BADGE_ELEMENT)
            return int(cart_badge.text)
        except NoSuchElementException:
            return 0
