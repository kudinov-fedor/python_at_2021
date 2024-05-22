from typing import List
from .base_page import BasePage
from .locators import ShoppingCart, ProductPageLocator
from .base_element import PageElement
from selenium.common.exceptions import NoSuchElementException


class CartItems(PageElement):
    def remove_item(self) -> None:
        self.find_element(*ShoppingCart.BTN_REMOVE).click()


class CartBadge(PageElement):
    def cart_badge(self) -> int:
        cart = self.find_element(*ProductPageLocator.CART_CONTAINER)
        try:
            badge = cart.find_element(*ProductPageLocator.CART_BADGE)
            if badge.is_displayed():
                return int(badge.text)
        except NoSuchElementException:
            return 0


class CartPageItem(BasePage):

    def cart_badge(self) -> int:
        cart = self.find_element(*ProductPageLocator.CART_CONTAINER)
        try:
            badge = cart.find_element(*ProductPageLocator.CART_BADGE)
            if badge.is_displayed():
                return int(badge.text)
        except NoSuchElementException:
            return 0
    @property
    def cart_list(self) -> List[CartItems]:
        return [CartItems(item.driver) for item in self.find_elements(*ShoppingCart.CART_LIST)]
