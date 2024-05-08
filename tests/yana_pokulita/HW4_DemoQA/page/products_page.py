from selenium.common import NoSuchElementException
from tests.yana_pokulita.HW4_DemoQA.page.base_page import BasePage
from tests.yana_pokulita.HW4_DemoQA.page.base_element import ProductsElement
from tests.yana_pokulita.locators import ProductPageLocators
from tests.yana_pokulita.locators import CartLocators


class ProductsPage(BasePage):
    def get_products(self) -> list[ProductsElement]:
        elements = self.find_elements(*ProductPageLocators.Elements)
        return [ProductsElement(e) for e in elements]

    def get_cart_badge(self):
        cart = self.driver.find_element(*CartLocators.ShoppingCart)
        try:
            cart_badge = cart.find_element(*CartLocators.ShoppingCartBadge)
        except NoSuchElementException:
            return 0
        return int(cart_badge.text)

    def go_to_cart_page(self):
        self.click(*CartLocators.ShoppingCart)
