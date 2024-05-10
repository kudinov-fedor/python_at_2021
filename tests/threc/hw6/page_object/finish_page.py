from tests.threc.hw6.page_object.base_page import BasePage
from tests.threc.hw6.locators import LocFillForm


class FinishPage(BasePage):
    def get_finish_order_title(self) -> str:
        # find on the finish page title and get this title
        return self.text(self.find_element(*LocFillForm.finishOrderTitle))
