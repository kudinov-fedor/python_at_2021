from selenium.common import NoSuchElementException
from tests.vvashchu.pages.base_page import BasePage
from tests.vvashchu.locators import ProductPageLocators


class ProductsPage(BasePage):
    def get_products(self):
        return self.find_elements(*ProductPageLocators.product)

    def move_product_to_cart(self, index):
        self.get_products()[index].find_element(*ProductPageLocators.product_add_to_cart_btn).click()

    def get_cart_badge(self):
        cart = self.driver.find_element(*ProductPageLocators.cart)
        try:
            cart_badge = cart.find_element(*ProductPageLocators.cart_badge)
        except NoSuchElementException:
            return 0
        return int(cart_badge.text)

    def go_to_cart_page(self):
        self.click(*ProductPageLocators.cart)
