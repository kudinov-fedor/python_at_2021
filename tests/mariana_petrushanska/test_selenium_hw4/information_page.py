from tests.mariana_petrushanska.test_selenium_hw4.base_page import BasePage
from tests.mariana_petrushanska.test_selenium_hw4.locators import InformationPageLoc


class InformationPage(BasePage):

    def fill_in_delivery_form(self, name, surname, zip):
        self.driver.find_element(*InformationPageLoc.TXT_FIRST_NAME).send_keys(name)
        self.driver.find_element(*InformationPageLoc.TXT_LAST_NAME).send_keys(surname)
        self.driver.find_element(*InformationPageLoc.TXT_POSTAL_CODE).send_keys(zip)

    def go_to_overview_page(self):
        self.driver.find_element(*InformationPageLoc.BTN_CONTINUE).click()
