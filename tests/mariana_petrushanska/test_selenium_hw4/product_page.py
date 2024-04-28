from tests.mariana_petrushanska.test_selenium_hw4.base_page import BasePage
from tests.mariana_petrushanska.test_selenium_hw4.locators import ProductsPageLoc


class ProductsPage(BasePage):

    def get_available_items(self):
        items = self.driver.find_elements(*ProductsPageLoc.LST_ITEMS)
        return items

    def get_separate_item(self, index):
        item = self.get_available_items()[index]
        return item

    def add_to_cart(self, item):
        item.find_element(*ProductsPageLoc.BTN_ADD_TO_CART).click()
