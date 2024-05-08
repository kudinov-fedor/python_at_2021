from tests.threc.hw6.locators import LocFillForm
from tests.threc.hw6.page_object.base_page import BasePage


class CheckoutPage(BasePage):
    def fill_form(self, first_name: str, last_name: str, zip_code: str):
        # fill checkout form
        self.find_element(*LocFillForm.firstName).send_keys(first_name)
        self.find_element(*LocFillForm.lastName).send_keys(last_name)
        self.find_element(*LocFillForm.zipCode).send_keys(zip_code)
        return self
