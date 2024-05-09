from tests.vvashchu.pages.base_page import BasePage
from tests.vvashchu.locators import CartLocators


class CheckoutCompletePage(BasePage):

    def back_to_products(self):
        self.click(*CartLocators.back_home_btn)
