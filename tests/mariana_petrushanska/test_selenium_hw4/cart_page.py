from tests.mariana_petrushanska.test_selenium_hw4.base_page import BasePage
from tests.mariana_petrushanska.test_selenium_hw4.locators import CartItemsLoc


class CartPage(BasePage):

    def get_items_in_cart(self):
        items = self.driver.find_elements(*CartItemsLoc.LST_CART_ITEMS)
        return items

    def remove_item(self, item):
        item.find_element(*CartItemsLoc.BTN_REMOVE_SECOND_ITEM).click()

    def check_checkout_btn(self):
        return self.driver.find_element(*CartItemsLoc.BTN_CHECKOUT).is_enabled()

    def go_to_checkout_page(self):
        self.driver.find_element(*CartItemsLoc.BTN_CHECKOUT).click()
