from tests.ysemenov.hw6.pages.base_page import BasePage
from tests.ysemenov.hw6.locators import LocatorsOverviewPage


class OverviewPage(BasePage):

    def finish_order(self):
        from tests.ysemenov.hw6.pages import OrderStatusPage
        self.click_by_locator(*LocatorsOverviewPage.BTN_FINISH)
        return OrderStatusPage(self.driver)
