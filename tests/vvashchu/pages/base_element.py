from selenium.webdriver.remote.webelement import WebElement
from typing import List
from tests.vvashchu.locators import ProductPageLocators
from tests.vvashchu.locators import CartLocators


class BaseElement:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, locator) -> WebElement:
        return self.driver.find_element(by, locator)

    def find_elements(self, by, locator) -> List[WebElement]:
        return self.driver.find_elements(by, locator)


class ProductsElement(BaseElement):

    def get_name(self) -> str:
        return self.find_element(*ProductPageLocators.product).text

    def add_to_cart(self):
        return self.find_element(*ProductPageLocators.product_add_to_cart_btn).click()


class CartElement(BaseElement):

    def remove_cart_item(self):
        return self.find_element(*CartLocators.remove_first_item_btn).click()
