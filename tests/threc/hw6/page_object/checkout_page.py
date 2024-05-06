from tests.threc.hw6.page_object.base_page import BasePage
from tests.threc.hw6.page_element.base_element import BaseElement
from tests.threc.hw6.locators import LocFillForm
from tests.threc.hw6.page_element.base_element import FinishElement


class CheckoutPage(BasePage, BaseElement):
    def fill_form(self, first_name: str, last_name: str, zip_code: str):
        # fill checkout form
        self.find_element(*LocFillForm.firstName).send_keys(first_name)
        self.find_element(*LocFillForm.lastName).send_keys(last_name)
        self.find_element(*LocFillForm.zipCode).send_keys(zip_code)
        return self

    def find_and_click_submit_btn(self):
        # submit checkout form
        self.click(self.find_element(*LocFillForm.btnContinue))
        return self

    def find_and_click_finish_btn(self) -> FinishElement:
        # find finish button and click it
        self.click(self.find_element(*LocFillForm.btnFinish))
        return FinishElement(self.driver)
