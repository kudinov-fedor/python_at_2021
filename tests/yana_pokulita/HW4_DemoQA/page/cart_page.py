from selenium.common import NoSuchElementException

from tests.yana_pokulita.HW4_DemoQA.page.base_page import BasePage
from tests.yana_pokulita.locators import CartLocators


class CartPage(BasePage):
    def get_cart_elements(self):
        cart_elements = self.driver.find_elements(*CartLocators.ShoppingCart)
        return cart_elements

    def get_cart_badge(self):
        # cart_badge = self.driver.find_element(*CartLocators.ShoppingCartBadge)
        # return cart_badge
        cart = self.driver.find_element(*CartLocators.ShoppingCart)
        try:
            cart_badge = cart.find_element(*CartLocators.ShoppingCartBadge)
        except NoSuchElementException:
            return 0
        return int(cart_badge.text)

    def go_to_cart_page(self):
        self.driver.find_element(*CartLocators.ShoppingCart).click()

    def get_cart_items(self):
        cart_items = self.driver.find_elements(*CartLocators.CartItems)
        return cart_items

    def go_to_checkout_page(self):
        self.driver.find_element(*CartLocators.CheckOutBtn).click()

    def remove_cart_item(self, index):
        # items = self.driver.find_elements(*CartLocators.CartItems)
        # items[index].find_element(*CartLocators.RemoveItemBtn).click()
        items = self.get_cart_items()
        items[index].find_element(*CartLocators.RemoveItemBtn).click()

    def is_checkout_enabled(self):
        checkout_btn = self.driver.find_element(*CartLocators.CheckOutBtn).is_enabled()
        return checkout_btn
