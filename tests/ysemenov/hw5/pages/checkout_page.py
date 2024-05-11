from tests.ysemenov.hw5.pages.base_page import BasePage
from tests.ysemenov.hw5.locators import LocatorsCheckoutPage


class CheckoutPage(BasePage):

    def submit_checkout_details(self, firstname, lastname, postal_code):
        self.send_keys(*LocatorsCheckoutPage.TXT_FIRST_NAME, firstname)
        self.send_keys(*LocatorsCheckoutPage.TXT_LAST_NAME, lastname)
        self.send_keys(*LocatorsCheckoutPage.TXT_POSTAL_CODE, postal_code)
        self.click_by_locator(*LocatorsCheckoutPage.BTN_CONTINUE)
