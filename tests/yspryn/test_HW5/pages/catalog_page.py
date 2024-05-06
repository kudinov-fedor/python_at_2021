from tests.yspryn.test_HW5.pages.base_page import BasePage
from tests.yspryn.test_HW5.pages import locators
from selenium.common import NoSuchElementException


class CatalogPage(BasePage):
    def get_number_of_available_items(self) -> int:
        elements = self.find_elements(*locators.LandingPage.TABLE_PRODUCT_ITEMS)
        return len(elements)

    def go_to_cart(self):
        cart = self.find_element(*locators.LandingPage.BTN_CART_LOCATE)
        cart.click()

    def check_number_of_items_added_to_cart(self) -> int:
        cart = self.find_element(*locators.LandingPage.BTN_CART_LOCATE)
        try:
            cart_badge = cart.find_element(*locators.LandingPage.TXT_CART_BADGE)
        except NoSuchElementException:
            return 0
        return int(cart_badge.text)

    def get_list_of_products_to_buy(self) -> list:
        return self.find_elements(*locators.LandingPage.TABLE_PRODUCT_ITEMS)

    def add_product_to_cart(self, index: int):
        items_list = self.get_list_of_products_to_buy()
        items_list[index].find_element(*locators.LandingPage.BTN_ADD_TO_CART).click()
