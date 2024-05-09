from tests.innahoncharenko.homework_6.pages.locators import CartLocators
from selenium.common import NoSuchElementException


class CartElement:
    def __init__(self, web_element):
        self.element = web_element

    def open_cart_page(self):
        self.element.click()
        from tests.innahoncharenko.homework_6.pages.cart_page import CartPage
        return CartPage(self.element.parent)

    @property
    def items_in_cart_number(self):
        try:
            cart_badge = self.element.find_element(*CartLocators.CART_BADGE_ELEMENT)
            return int(cart_badge.text)
        except NoSuchElementException:
            return 0
