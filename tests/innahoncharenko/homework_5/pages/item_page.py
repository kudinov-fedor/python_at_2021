from tests.innahoncharenko.homework_5.pages.base_page import BasePage
from tests.innahoncharenko.homework_5.pages.locators import CartLocators
from tests.innahoncharenko.homework_5.pages.locators import InventoryItemsLocators
from tests.innahoncharenko.homework_5.pages.cart_page import CartPage
from selenium.common import NoSuchElementException


class ItemPage(BasePage):
    # Will return Cart page
    def open_cart(self):
        self.click_element(CartLocators.CART)
        return CartPage(self.driver)

    def add_to_cart(self):
        self.click_element(InventoryItemsLocators.ADD_TO_CART_BUTTON)

    def remove_from_cart(self):
        self.click_element(InventoryItemsLocators.REMOVE_BUTTON)

    def get_items_in_cart_number(self):
        cart = self.find_element(CartLocators.CART)
        try:
            cart_badge = cart.find_element(*CartLocators.CART_BADGE_ELEMENT)
            return int(cart_badge.text)
        except NoSuchElementException:
            return 0
