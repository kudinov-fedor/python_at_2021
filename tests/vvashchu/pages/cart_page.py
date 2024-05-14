from tests.vvashchu.pages.base_page import BasePage
from typing import List
from tests.vvashchu.pages.base_element import CartElement
from tests.vvashchu.locators import CartLocators


class CartPage(BasePage):

    def get_cart_items(self) -> List[CartElement]:
        elements = self.find_elements(*CartLocators.cart_items)
        return [CartElement(e) for e in elements]

    def go_to_checkout_page(self):
        self.click(*CartLocators.checkout_btn)

    def remove_cart_item(self, index):
        items = self.get_cart_items()
        items[index].find_element(*CartLocators.remove_first_item_btn).click()

    def is_checkout_enabled(self):
        checkout_btn = self.find_element(*CartLocators.checkout_btn).is_enabled()
        return checkout_btn
