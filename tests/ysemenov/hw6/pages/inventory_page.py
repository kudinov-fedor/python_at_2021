from selenium.webdriver.remote.webelement import WebElement
from tests.ysemenov.hw6.pages.base_page import BasePage, BaseElement
from tests.ysemenov.hw6.pages.product_details_page import ProductDetailsPage
from tests.ysemenov.hw6.locators import LocatorsInventoryPage


class InventoryPageItem(BaseElement):

    def __init__(self, web_element: WebElement):
        super().__init__(web_element)

    def add_to_cart(self):
        self.find_element(*LocatorsInventoryPage.BTN_ADD_TO_CART).click()


class InventoryPage(BasePage):

    @property
    def products(self) -> list[InventoryPageItem]:
        elements = self.find_elements(*LocatorsInventoryPage.LST_INVENTORY)
        return [InventoryPageItem(element.element) for element in elements]

    def open_product_page(self, product: InventoryPageItem) -> ProductDetailsPage:
        product.find_element(*LocatorsInventoryPage.LNK_PRODUCT_NAME).click()
        return ProductDetailsPage(self.driver)
