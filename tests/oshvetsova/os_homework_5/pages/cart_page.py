from .base_page import BasePage
from .locators import *
from selenium.common.exceptions import NoSuchElementException


class CartPage(BasePage):

    def remove_item(self, index):
        items = self.driver.find_elements(*ShoppingCart.CART_LIST)
        items[index].find_element(*ShoppingCart.BTN_REMOVE).click()

    def cart_badge(self):
        cart = self.driver.find_element(*ProductPageLocator.CART_CONTAINER)
        try:
            cart.find_element(*ProductPageLocator.CART_BADGE).is_displayed()
        except NoSuchElementException:
            return 0
        return 1
