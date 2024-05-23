from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from tests.ysemenov.hw6.pages.base_page import BasePage, BaseElement
from tests.ysemenov.hw6.pages.product_details_page import ProductDetailsPage
from tests.ysemenov.hw6.locators import LocatorsInventoryPage


class InventoryPageItem(BaseElement):

    def __init__(self, element: WebElement, driver: WebDriver):
        super().__init__(element)
        self.driver = driver

    def add_to_cart(self):
        self.find_element(*LocatorsInventoryPage.BTN_ADD_TO_CART).click()

    def open_product_page(self) -> ProductDetailsPage:
        self.find_element(*LocatorsInventoryPage.LNK_PRODUCT_NAME).click()
        return ProductDetailsPage(self.driver)


class InventoryPage(BasePage):

    @property
    def products(self) -> list[InventoryPageItem]:
        elements = self.find_elements(*LocatorsInventoryPage.LST_INVENTORY)
        return [InventoryPageItem(element.element, self.driver) for element in elements]
