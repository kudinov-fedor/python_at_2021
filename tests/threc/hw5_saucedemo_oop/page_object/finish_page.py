from tests.threc.hw5_saucedemo_oop.page_object.base_page import BasePage
from tests.threc.hw5_saucedemo_oop.locators import LocFillForm


class FinishPage(BasePage):
    def finish_order_title(self):
        # find on the finish page title and get this title
        return self.find_element(*LocFillForm.finishOrderTitle).text
