from tests.innahoncharenko.homework_6.pages.base_page import BasePage
from tests.innahoncharenko.homework_6.pages.locators import CheckoutPageLocators
from tests.innahoncharenko.homework_6.pages.finish_page import FinishPage


class CheckoutPage(BasePage):
    # Will return Finish Page
    def fill_form_and_continue(self, first_name, last_name, postal_code):
        self.find_element(CheckoutPageLocators.FIRST_NAME).send_keys(first_name)
        self.find_element(CheckoutPageLocators.LAST_NAME).send_keys(last_name)
        self.find_element(CheckoutPageLocators.POSTAL_CODE).send_keys(postal_code)
        self.click_element(CheckoutPageLocators.CONTINUE_BUTTON)
        return FinishPage(self.driver)
