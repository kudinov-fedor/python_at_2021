from tests.threc.hw6.page_object.base_page import BasePage
from tests.threc.hw6.page_object.checkout_page import CheckoutPage
from tests.threc.hw6.locators import LocCartPage, LocCheckoutPage


class CartPage(BasePage):
    def open_cart(self):
        # open cart page
        return self.click(self.find_element(*LocCartPage.cartLink))

    def click_continue_btn(self):
        # find button continue and click it
        self.click(self.find_element(*LocCheckoutPage.btnContinueShopping))

    def click_checkout_btn(self) -> CheckoutPage:
        # find button checkout and click it
        self.click(self.find_element(*LocCheckoutPage.btnCheckout))
        return CheckoutPage(self.driver)
