from tests.threc.hw6.page_object.base_page import BasePage
from tests.threc.hw6.page_element.base_element import BaseElement
from tests.threc.hw6.locators import LocCartPage, LocCheckoutPage
from tests.threc.hw6.page_object.product_page import ProductPage
from tests.threc.hw6.page_object.checkout_page import CheckoutPage


class CartPage(BasePage, BaseElement):

    def open_cart(self):
        # open cart page
        return self.click(self.find_element(*LocCartPage.cartLink))

    def find_and_click_continue_btn(self):
        # find button continue and click it
        self.click(self.find_element(*LocCheckoutPage.btnContinueShopping))
        return ProductPage(self.driver)

    def find_and_click_checkout_btn(self) -> CheckoutPage:
        # find button checkout and click it
        self.click(self.find_element(*LocCheckoutPage.btnCheckout))
        return CheckoutPage(self.driver)
