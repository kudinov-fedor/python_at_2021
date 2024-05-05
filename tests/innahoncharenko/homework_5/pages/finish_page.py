from tests.innahoncharenko.homework_5.pages.base_page import BasePage
from tests.innahoncharenko.homework_5.pages.locators import CheckoutPageLocators


class FinishPage(BasePage):
    def finish(self):
        self.click_element(CheckoutPageLocators.FINISH_BUTTON)
