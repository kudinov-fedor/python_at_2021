from tests.yana_pokulita.HW4_DemoQA.page.base_page import BasePage
from tests.yana_pokulita.locators import CartLocators


class CheckoutInformationPage(BasePage):

    def fill_order_form(self, first_name, last_name, postal_code):
        self.driver.find_element(*CartLocators.FirstName).send_keys(first_name)
        self.driver.find_element(*CartLocators.LastName).send_keys(last_name)
        self.driver.find_element(*CartLocators.PostalCode).send_keys(postal_code)
        self.driver.find_element(*CartLocators.btnContinue).click()
