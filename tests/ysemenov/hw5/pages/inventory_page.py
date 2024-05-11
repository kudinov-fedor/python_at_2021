from selenium.webdriver.remote.webelement import WebElement
from tests.ysemenov.hw5.pages.base_page import BasePage
from tests.ysemenov.hw5.locators import LocatorsInventoryPage


class InventoryPage(BasePage):

    def get_products(self) -> list[WebElement]:
        return self.find_elements(*LocatorsInventoryPage.LST_INVENTORY)

    def add_product_to_cart(self, product: WebElement):
        product.find_element(*LocatorsInventoryPage.BTN_ADD_TO_CART).click()

    def open_product_page(self, product: WebElement):
        product.find_element(*LocatorsInventoryPage.LNK_PRODUCT_NAME).click()
