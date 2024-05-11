from tests.mariana_petrushanska.test_selenium_hw5.base_page import BasePage
from tests.mariana_petrushanska.test_selenium_hw5.locators import OverviewPageLoc


class OverviewPage(BasePage):

    def finish_order(self):
        self.find_element(*OverviewPageLoc.BTN_FINISH).click()

    # def get_sum_of_prices(self):
    #     item_price = self.find_elements(*OverviewPageLoc.TXT_ITEM_PRICE)
    #     prices = [item.text for item in item_price]
    #     final_item_price = [float(price.replace('$', '')) for price in prices]
    #     calculated_total = sum(final_item_price)
    #     return calculated_total

    def get_items(self):
        items = self.find_elements(*OverviewPageLoc.LST_ITEMS_TO_BUY)
        return items

    def item_price(self, item):
        price = item.find_element(*OverviewPageLoc.TXT_ITEM_PRICE).text
        return float(price.replace('$', ''))

    def total(self):
        item_total = self.find_element(*OverviewPageLoc.TXT_ITEM_TOTAL).text
        return float(item_total.replace('Item total: $', ''))
