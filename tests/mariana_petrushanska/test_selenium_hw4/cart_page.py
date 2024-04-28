from tests.mariana_petrushanska.test_selenium_hw4.base_page import BasePage
from tests.mariana_petrushanska.test_selenium_hw4.locators import CartItemsLoc


class CartPage(BasePage):

    def get_cart_badge_number(self):
        cart = self.driver.find_element(*CartItemsLoc.IMG_CART)
        cart_badge = cart.find_element(*CartItemsLoc.IMG_CART_BADGE)
        return cart_badge.text

    def go_to_cart(self):
        self.driver.find_element(*CartItemsLoc.IMG_CART).click()

    def get_items_in_cart(self):
        items = self.driver.find_elements(*CartItemsLoc.LST_CART_ITEMS)
        return items

    def remove_item(self, items, index):
        items[index].find_element(*CartItemsLoc.BTN_REMOVE_SECOND_ITEM).click()

    def check_checkout_btn(self):
        checkout_availability = self.driver.find_element(*CartItemsLoc.BTN_CHECKOUT).is_enabled()
        return checkout_availability

    def go_to_checkout_page(self):
        self.driver.find_element(*CartItemsLoc.BTN_CHECKOUT).click()
