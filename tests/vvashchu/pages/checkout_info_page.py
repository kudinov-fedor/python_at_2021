from tests.vvashchu.pages.base_page import BasePage
from tests.vvashchu.locators import CartLocators


class CheckoutInfoPage(BasePage):

    def fill_order_form(self, first_name, last_name, postal_code):
        self.driver.find_element(*CartLocators.FirstName).send_keys(first_name)
        self.driver.find_element(*CartLocators.LastName).send_keys(last_name)
        self.driver.find_element(*CartLocators.PostalCode).send_keys(postal_code)
        self.click(*CartLocators.continue_btn)
