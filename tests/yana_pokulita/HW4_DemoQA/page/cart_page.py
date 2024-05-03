from tests.yana_pokulita.HW4_DemoQA.page.base_page import BasePage
from tests.yana_pokulita.locators import CartLocators


class CartPage(BasePage):

    def get_cart_items(self):
        return self.find_elements(*CartLocators.CartItems)

    def go_to_checkout_page(self):
        self.click(*CartLocators.CheckOutBtn)

    def remove_cart_item(self, index):
        items = self.get_cart_items()
        items[index].find_element(*CartLocators.RemoveItemBtn).click()

    def is_checkout_enabled(self):
        checkout_btn = self.find_element(*CartLocators.CheckOutBtn).is_enabled()
        return checkout_btn
