from tests.mariana_petrushanska.test_selenium_hw5.base_page import BasePage
from tests.mariana_petrushanska.test_selenium_hw5.locators import SuccessPageLoc


class SuccessPage(BasePage):

    def go_to_homepage(self):
        self.find_element(*SuccessPageLoc.BTN_BACK_HOME).click()
