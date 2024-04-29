from tests.threc.hw5_saucedemo_oop.page_object.base_page import BasePage
from tests.threc.hw5_saucedemo_oop.locators import LocFillForm
from tests.threc.hw5_saucedemo_oop.locators import LocCheckoutPage


class CheckoutPage(BasePage):
    def checkout_fill_form(self, first_name: str, last_name: str, zip_code: str):
        self.driver.find_element(*LocFillForm.firstName).send_keys(first_name)
        self.driver.find_element(*LocFillForm.lastName).send_keys(last_name)
        self.driver.find_element(*LocFillForm.zipCode).send_keys(zip_code)

    def checkout_submit_btn(self):
        submit_btn = self.driver.find_element(*LocFillForm.btnContinue)
        return submit_btn

    def checkout_product_label(self):
        label = self.driver.find_element(*LocCheckoutPage.checkoutItem)
        return label.text

    def checkout_finish_btn(self):
        finish_btn = self.driver.find_element(*LocFillForm.btnFinish)
        return finish_btn

    def checkout_btn_click(self, button):
        button.click()
