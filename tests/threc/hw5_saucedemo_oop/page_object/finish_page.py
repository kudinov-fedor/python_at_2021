from tests.threc.hw5_saucedemo_oop.page_object.base_page import BasePage
from tests.threc.hw5_saucedemo_oop.locators import LocFillForm


class FinishPage(BasePage):
    def get_finish_order_title(self):
        # find on the finish page title and get this title
        return self.text(*LocFillForm.finishOrderTitle)
