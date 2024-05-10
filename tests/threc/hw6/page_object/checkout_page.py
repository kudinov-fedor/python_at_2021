from tests.threc.hw6.locators import LocFillForm, LocCheckoutPage
from tests.threc.hw6.page_object.base_page import BasePage
from tests.threc.hw6.page_object.finish_page import FinishPage
from typing import List

from tests.threc.hw6.page_element.base_element import CheckoutElement


class CheckoutPage(BasePage):
    def fill_form(self, first_name: str, last_name: str, zip_code: str):
        # fill checkout form
        self.find_element(*LocFillForm.firstName).send_keys(first_name)
        self.find_element(*LocFillForm.lastName).send_keys(last_name)
        self.find_element(*LocFillForm.zipCode).send_keys(zip_code)
        return self

    def click_submit_btn(self):
        # submit checkout form
        self.click(self.find_element(*LocFillForm.btnContinue))
        return self

    def click_finish_btn(self) -> FinishPage:
        # find finish button and click it
        self.click(self.find_element(*LocFillForm.btnFinish))
        return FinishPage(self.driver)

    def get_added_products(self) -> List[CheckoutElement]:
        # List of added products to the cart on the overview
        added_products = []
        for p in self.find_elements(*LocCheckoutPage.addedProducts):
            added_products.append(CheckoutElement(p))
        return added_products
