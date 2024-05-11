from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from tests.yspryn.test_HW6.pages import locators


class BaseElement:
    def __init__(self, driver: WebElement):
        self.driver = driver

    def parent(self) -> WebDriver:
        return self.driver.parent

    def find_element(self, by: str, locator: str) -> WebElement:
        return self.driver.find_element(by, locator)

    def find_elements(self, by: str, locator: str) -> list[WebElement]:
        return self.driver.find_elements(by, locator)


class CatalogElement(BaseElement):
    def add_item_to_cart(self):
        return self.find_element(*locators.LandingPage.BTN_ADD_TO_CART).click()

    def get_price(self) -> str:
        return self.find_element(*locators.LandingPage.TXT_ITEM_PRICE).text

    def get_product_name(self) -> str:
        return self.find_element(*locators.LandingPage.TXT_ITEM_NAME).text


class CartElement(BaseElement):
    def remove_cart_item(self):
        return self.find_element(*locators.CartPage.BTN_REMOVE_FROM_CART).click()
