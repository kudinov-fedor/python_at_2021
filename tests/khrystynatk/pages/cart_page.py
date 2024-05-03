from tests.khrystynatk.pages.base_page import BasePage
from tests.khrystynatk.pages.locators1 import CartItemsLoc
from selenium.common import NoSuchElementException
from tests.khrystynatk.pages.base_elements import CartElement


class CartPage(BasePage):

    def find_cart_rows(self) -> list[CartElement]:
        elements = self.driver.find_elements(*CartItemsLoc.CART_ITEMS)
        return [CartElement(el) for el in elements]

    def get_cart_badge(self):
        cart = self.driver.find_element(*CartItemsLoc.CART_CONTAINER)
        try:
            cart_badge = cart.find_element(*CartItemsLoc.IMG_CART_BADGE)
        except NoSuchElementException:
            return 0
        return int(cart_badge.text)
