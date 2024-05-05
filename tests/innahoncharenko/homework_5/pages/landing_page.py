from tests.innahoncharenko.homework_5.pages.base_page import BasePage
from tests.innahoncharenko.homework_5.pages.locators import CartLocators
from tests.innahoncharenko.homework_5.pages.locators import InventoryItemsLocators
from tests.innahoncharenko.homework_5.pages.item_page import ItemPage
from tests.innahoncharenko.homework_5.pages.cart_page import CartPage
from selenium.common import NoSuchElementException


class LandingPage(BasePage):
    # Will return Cart page
    def open_cart(self):
        self.click_element(CartLocators.CART)
        return CartPage(self.driver)

    # Will return Item Page
    def open_item(self, item_index):
        item = self.find_elements(InventoryItemsLocators.INVENTORY_ITEMS)[item_index]
        item_name = item.find_element(*InventoryItemsLocators.INVENTORY_ITEM_NAME)
        item_name.click()
        return ItemPage(self.driver)

    def click_element_action_button(self, item_index):
        item = self.find_elements(InventoryItemsLocators.INVENTORY_ITEMS)[item_index]
        button = item.find_element(*InventoryItemsLocators.BUTTON)
        button.click()

    def add_item_to_cart(self, item_index):
        self.click_element_action_button(item_index)

    def remove_item_from_cart(self, item_index):
        self.click_element_action_button(item_index)

    def get_items_number(self):
        return len(self.find_elements(InventoryItemsLocators.INVENTORY_ITEMS))

    def get_items_in_cart_number(self):
        cart = self.find_element(CartLocators.CART)
        try:
            cart_badge = cart.find_element(*CartLocators.CART_BADGE_ELEMENT)
            return int(cart_badge.text)
        except NoSuchElementException:
            return 0
