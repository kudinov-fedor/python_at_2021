from .base_page import BasePage
from .locators import ShoppingCart, ProductPageLocator
from .base_element import PageElement
from selenium.common.exceptions import NoSuchElementException


class CartItems(PageElement):
    def remove_item(self, index: int) -> None:
        items = self.find_elements(*ShoppingCart.CART_LIST)
        items[index].find_element(*ShoppingCart.BTN_REMOVE).click()


class CartBadge(PageElement):
    def cart_badge(self) -> int:
        cart = self.find_element(*ProductPageLocator.CART_CONTAINER)
        try:
            cart.find_element(*ProductPageLocator.CART_BADGE).is_displayed()
        except NoSuchElementException:
            return 0
        return 1


class CartPageItem(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.cart_items = CartItems(driver)
        self.cart_badge = CartBadge(driver)

    def remove_item(self, index: int) -> None:
        self.cart_items.remove_item(index)

    def cart_badge(self) -> int:
        return self.cart_badge.cart_badge()

    def __getattr__(self, item):
        try:
            return self.__dict__[item]
        except KeyError:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{item}'")