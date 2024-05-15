from selenium.webdriver.remote.webelement import WebElement
from tests.mariana_petrushanska.test_selenium_hw5.locators import ProductsPageLoc, CartItemsLoc, OverviewPageLoc


class BaseElement:

    def __init__(self, driver: WebElement):
        self.driver = driver

    def parent(self) -> WebElement:
        return self.driver.parent

    def find_element(self, by, locator) -> WebElement:
        return self.driver.find_element(by, locator)

    def find_elements(self, by, locator) -> list[WebElement]:
        return self.driver.find_elements(by, locator)


class ProductsPageItem(BaseElement):

    def add_to_cart(self):
        self.find_element(*ProductsPageLoc.BTN_ADD_TO_CART).click()


class CartPageItem(BaseElement):

    def remove_item(self):
        self.find_element(*CartItemsLoc.BTN_REMOVE_ITEM).click()


class OverviewPageItem(BaseElement):

    @property
    def price(self) -> float:
        price = self.find_element(*OverviewPageLoc.TXT_ITEM_PRICE).text
        return float(price.replace('$', ''))