from selenium.common import NoSuchElementException
from typing import List
from tests.vvashchu.pages.base_page import BasePage
from tests.vvashchu.pages.base_element import ProductsElement
from tests.vvashchu.locators import ProductPageLocators


class ProductsPage(BasePage):

    def get_products(self) -> List[ProductsElement]:
        elements = self.find_elements(*ProductPageLocators.product)
        return [ProductsElement(e) for e in elements]

    def get_cart_badge(self):
        cart = self.driver.find_element(*ProductPageLocators.cart)
        try:
            cart_badge = cart.find_element(*ProductPageLocators.cart_badge)
        except NoSuchElementException:
            return 0
        return int(cart_badge.text)

    def go_to_cart_page(self):
        self.click(*ProductPageLocators.cart)
