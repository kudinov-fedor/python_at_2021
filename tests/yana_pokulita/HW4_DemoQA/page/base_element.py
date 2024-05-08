from selenium.webdriver.remote.webelement import WebElement
from tests.yana_pokulita.locators import ProductPageLocators
from tests.yana_pokulita.locators import CartLocators


class BaseElement:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, locator) -> WebElement:
        return self.driver.find_element(by, locator)

    def find_elements(self, by, locator) -> list[WebElement]:
        return self.driver.find_elements(by, locator)


class ProductsElement(BaseElement):

    def get_product_name(self) -> str:
        return self.find_element(*ProductPageLocators.Element).text

    def add_to_cart(self):
        return self.find_element(*ProductPageLocators.Element).click()


class CartElement(BaseElement):

    def get_cart_item(self):
        return self.find_element(*CartLocators.CartItem)

    def remove_cart_item(self):
        return self.find_element(*CartLocators.RemoveItemBtn).click()
