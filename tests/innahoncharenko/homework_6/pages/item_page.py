from tests.innahoncharenko.homework_6.pages.base_page import BasePage
from tests.innahoncharenko.homework_6.pages.locators import CartLocators
from tests.innahoncharenko.homework_6.pages.locators import InventoryItemsLocators
from tests.innahoncharenko.homework_6.pages.cart_page import CartPage
from tests.innahoncharenko.homework_6.pages.cart_element import CartElement
from selenium.common import NoSuchElementException


class ItemPage(BasePage):
    def add_to_cart(self):
        self.click_element(InventoryItemsLocators.ADD_TO_CART_BUTTON)

    def remove_from_cart(self):
        self.click_element(InventoryItemsLocators.REMOVE_BUTTON)

    @property
    def cart_element(self):
        return CartElement(self.find_element(CartLocators.CART))
