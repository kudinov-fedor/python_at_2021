from typing import Self
from tests.mariana_petrushanska.test_selenium_hw5 import BasePage
from tests.mariana_petrushanska.test_selenium_hw5.locators import InformationPageLoc


class InformationPage(BasePage):

    def fill_in_delivery_form(self, name: str, surname: str, zip: str) -> Self:
        """
        Fill in user's information for delivery
        """
        self.find_element(*InformationPageLoc.TXT_FIRST_NAME).send_keys(name)
        self.find_element(*InformationPageLoc.TXT_LAST_NAME).send_keys(surname)
        self.find_element(*InformationPageLoc.TXT_POSTAL_CODE).send_keys(zip)
        return self

    def submit_form(self):
        """
        Submit delivery form
        """
        from tests.mariana_petrushanska.test_selenium_hw5 import OverviewPage

        self.find_element(*InformationPageLoc.BTN_CONTINUE).click()
        return OverviewPage(self.driver)
