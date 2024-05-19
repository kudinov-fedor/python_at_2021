from selenium.webdriver.chrome.webdriver import WebDriver
from tests.ysemenov.hw6.pages.base_page import BasePage, BaseElement
from tests.ysemenov.hw6.pages.product_details_page import ProductDetailsPage
from tests.ysemenov.hw6.locators import LocatorsInventoryPage


class InventoryPageItem(BaseElement):

    def add_to_cart(self):
        self.find_element(*LocatorsInventoryPage.BTN_ADD_TO_CART).click()

    def open_product_page(self, driver: WebDriver) -> ProductDetailsPage:
        self.find_element(*LocatorsInventoryPage.LNK_PRODUCT_NAME).click()
        return ProductDetailsPage(driver)


class InventoryPage(BasePage):

    @property
    def products(self) -> list[InventoryPageItem]:
        elements = self.find_elements(*LocatorsInventoryPage.LST_INVENTORY)
        return [InventoryPageItem(element.element) for element in elements]
