from tests.vvashchu.pages.base_page import BasePage
from tests.vvashchu.locators import CartLocators


class CheckoutOverviewPage(BasePage):

    def finish_order(self):
        self.click(*CartLocators.finish_btn)
