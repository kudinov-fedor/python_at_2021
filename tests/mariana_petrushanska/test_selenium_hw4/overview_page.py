from tests.mariana_petrushanska.test_selenium_hw4.base_page import BasePage
from tests.mariana_petrushanska.test_selenium_hw4.locators import OverviewPageLoc


class OverviewPage(BasePage):

    def finish_order(self):
        self.driver.find_element(*OverviewPageLoc.BTN_FINISH).click()

    def get_sum_of_prices(self):
        item_price = self.driver.find_elements(*OverviewPageLoc.TXT_ITEM_PRICE)
        prices = [item.text for item in item_price]
        final_item_price = [float(price.replace('$', '')) for price in prices]
        calculated_total = sum(final_item_price)
        return calculated_total

    def get_item_total(self):
        item_total = self.driver.find_element(*OverviewPageLoc.TXT_ITEM_TOTAL).text
        item_total = float(item_total.replace('Item total: $', ''))
        return item_total
