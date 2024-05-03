from tests.threc.hw5_saucedemo_oop.page_object.base_page import BasePage
from tests.threc.hw5_saucedemo_oop.locators import LocFillForm, LocCheckoutPage


class CheckoutPage(BasePage):
    def fill_form(self, first_name: str, last_name: str, zip_code: str):
        # fill checkout form
        self.find_element(*LocFillForm.firstName).send_keys(first_name)
        self.find_element(*LocFillForm.lastName).send_keys(last_name)
        self.find_element(*LocFillForm.zipCode).send_keys(zip_code)

    def find_and_click_submit_btn(self):
        # submit checkout form
        self.click(self.find_element(*LocFillForm.btnContinue))

    def find_and_get_product_label(self):
        # find product name and get this name
        return self.text(*LocCheckoutPage.checkoutItem)

    def find_and_click_finish_btn(self):
        # find finish button and click it
        self.click(self.find_element(*LocFillForm.btnFinish))
