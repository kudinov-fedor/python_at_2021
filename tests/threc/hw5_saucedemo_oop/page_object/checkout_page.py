from tests.threc.hw5_saucedemo_oop.page_object.base_page import BasePage
from tests.threc.hw5_saucedemo_oop.locators import LocFillForm
from tests.threc.hw5_saucedemo_oop.locators import LocCheckoutPage


class CheckoutPage(BasePage):
    def checkout_fill_form(self, first_name: str, last_name: str, zip_code: str):
        self.find_elem(*LocFillForm.firstName).send_keys(first_name)
        self.find_elem(*LocFillForm.lastName).send_keys(last_name)
        self.find_elem(*LocFillForm.zipCode).send_keys(zip_code)

    def checkout_submit_btn(self):
        submit_btn = self.find_elem(*LocFillForm.btnContinue)
        return submit_btn

    def checkout_product_label(self):
        label = self.find_elem(*LocCheckoutPage.checkoutItem)
        return label.text

    def checkout_finish_btn(self):
        finish_btn = self.find_elem(*LocFillForm.btnFinish)
        return finish_btn
