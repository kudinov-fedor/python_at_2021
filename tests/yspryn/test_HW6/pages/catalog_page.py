from tests.yspryn.test_HW6.pages.base_page import BasePage
from tests.yspryn.test_HW6.pages import locators
from selenium.common import NoSuchElementException
from tests.yspryn.test_HW6.pages.base_elements import CatalogElement


class CatalogPage(BasePage):
    def go_to_cart(self):
        from tests.yspryn.test_HW6.pages.cart_page import CartPage

        cart = self.find_element(*locators.LandingPage.BTN_CART_LOCATE)
        cart.click()
        return CartPage(self.driver)

    def check_number_of_items_added_to_cart(self) -> int:
        cart = self.find_element(*locators.LandingPage.BTN_CART_LOCATE)
        try:
            cart_badge = cart.find_element(*locators.LandingPage.TXT_CART_BADGE)
        except NoSuchElementException:
            return 0
        return int(cart_badge.text)

    def list_of_products_to_buy(self) -> list[CatalogElement]:
        products_to_buy = self.find_elements(*locators.LandingPage.TABLE_PRODUCT_ITEMS)
        return [CatalogElement(el) for el in products_to_buy]
