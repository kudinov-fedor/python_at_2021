from tests.ysemenov.hw5.pages.base_page import BasePage
from tests.ysemenov.hw5.locators import LocatorsOverviewPage


class OverviewPage(BasePage):

    def finish_order(self):
        self.click_by_locator(*LocatorsOverviewPage.BTN_FINISH)
