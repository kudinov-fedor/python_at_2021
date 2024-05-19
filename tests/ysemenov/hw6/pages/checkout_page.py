from tests.ysemenov.hw6.pages.base_page import BasePage
from tests.ysemenov.hw6.locators import LocatorsCheckoutPage


class CheckoutPage(BasePage):

    def submit_checkout_details(self, firstname: str, lastname: str, postal_code: str):
        from tests.ysemenov.hw6.pages import OverviewPage
        self.send_keys(*LocatorsCheckoutPage.TXT_FIRST_NAME, firstname)
        self.send_keys(*LocatorsCheckoutPage.TXT_LAST_NAME, lastname)
        self.send_keys(*LocatorsCheckoutPage.TXT_POSTAL_CODE, postal_code)
        self.click_by_locator(*LocatorsCheckoutPage.BTN_CONTINUE)
        return OverviewPage(self.driver)
