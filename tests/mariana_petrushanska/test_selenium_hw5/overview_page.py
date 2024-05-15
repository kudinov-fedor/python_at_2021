from tests.mariana_petrushanska.test_selenium_hw5.web_element import OverviewPageItem
from tests.mariana_petrushanska.test_selenium_hw5.base_page import BasePage
from tests.mariana_petrushanska.test_selenium_hw5.locators import OverviewPageLoc


class OverviewPage(BasePage):

    @property
    def items(self) -> list[OverviewPageItem]:
        items = self.find_elements(*OverviewPageLoc.LST_ITEMS_TO_BUY)
        return [OverviewPageItem(item) for item in items]

    @property
    def total(self) -> float:
        item_total = self.find_element(*OverviewPageLoc.TXT_ITEM_TOTAL).text
        return float(item_total.replace('Item total: $', ''))

    def finish_order(self):
        self.find_element(*OverviewPageLoc.BTN_FINISH).click()
