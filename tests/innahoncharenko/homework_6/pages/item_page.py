from tests.innahoncharenko.homework_6.pages.base_page import BasePage
from tests.innahoncharenko.homework_6.pages.locators import CartLocators
from tests.innahoncharenko.homework_6.pages.locators import InventoryItemsLocators
from tests.innahoncharenko.homework_6.pages.cart_page import CartPage
from tests.innahoncharenko.homework_6.pages.cart_element import CartElement
from selenium.common import NoSuchElementException


class ItemPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.cart_element = CartElement(self.driver)

    # Will return Cart page
    def open_cart(self):
        return self.cart_element.open_cart_page()

    def add_to_cart(self):
        self.click_element(InventoryItemsLocators.ADD_TO_CART_BUTTON)

    def remove_from_cart(self):
        self.click_element(InventoryItemsLocators.REMOVE_BUTTON)

    def get_items_in_cart_number(self):
        return self.cart_element.get_items_in_cart_number
