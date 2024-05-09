from tests.vvashchu.pages.base_page import BasePage
from tests.vvashchu.locators import CartLocators


class CartPage(BasePage):

    def get_cart_items(self):
        return self.find_elements(*CartLocators.cart_items)

    def go_to_checkout_page(self):
        self.click(*CartLocators.checkout_btn)

    def remove_cart_item(self, index):
        items = self.get_cart_items()
        items[index].find_element(*CartLocators.remove_first_item_btn).click()

    def is_checkout_enabled(self):
        checkout_btn = self.find_element(*CartLocators.checkout_btn).is_enabled()
        return checkout_btn
