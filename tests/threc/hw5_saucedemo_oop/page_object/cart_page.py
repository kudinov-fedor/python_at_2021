from tests.threc.hw5_saucedemo_oop.page_object.base_page import BasePage
from tests.threc.hw5_saucedemo_oop.locators import LocCartPage, LocCheckoutPage


class CartPage(BasePage):

    def open_cart(self):
        # open cart page
        return self.click(self.find_element(*LocCartPage.cartLink))

    def get_product_name(self):
        # get added to cart product name
        return self.text(self.find_element(*LocCartPage.cartProductName))

    def find_and_click_continue_btn(self):
        # find button continue and click it
        self.click(self.find_element(*LocCheckoutPage.btnContinueShopping))

    def find_and_click_checkout_btn(self):
        # find button checkout and click it
        self.click(self.find_element(*LocCheckoutPage.btnCheckout))
