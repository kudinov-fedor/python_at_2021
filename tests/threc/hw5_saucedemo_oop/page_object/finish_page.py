from tests.threc.hw5_saucedemo_oop.page_object.base_page import BasePage
from tests.threc.hw5_saucedemo_oop.locators import LocFillForm


class FinishPage(BasePage):
    def finish_title(self):
        finish_title = self.driver.find_element(*LocFillForm.finishOrderTitle)
        return finish_title.text