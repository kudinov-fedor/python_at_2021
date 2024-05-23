from tests.mariana_petrushanska.test_selenium_hw5.web_element import ProductsPageItem
from tests.mariana_petrushanska.test_selenium_hw5.base_page import BasePage
from tests.mariana_petrushanska.test_selenium_hw5.locators import ProductsPageLoc


class ProductsPage(BasePage):

    @property
    def available_items(self) -> list[ProductsPageItem]:
        items = self.find_elements(*ProductsPageLoc.LST_ITEMS)
        return [ProductsPageItem(item) for item in items]
