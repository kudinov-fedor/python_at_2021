from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from tests.khrystynatk.pages.locators1 import LandingPageLoc, CartItemsLoc


class BaseElement:
    def __init__(self, driver: WebElement):
        self.driver = driver

    def parent(self) -> WebDriver:
        return self.driver.parent

    def find_element(self, by, value) -> WebElement:
        return self.driver.find_element(by, value)

    def find_elements(self, by, value) -> list[WebElement]:
        return self.driver.find_elements(by, value)


class ProductsElement(BaseElement):

    def get_product_name(self) -> str:
        return self.find_element(*LandingPageLoc.LNK_OPEN_PRODUCT).text

    def get_price(self) -> float:
        price = self.find_element(*LandingPageLoc.TXT_PRODUCT_PRICE).text.replace("$", "")
        return float(price)

    def add_to_cart(self):
        return self.find_element(*LandingPageLoc.BTN_ADD_TO_CART).click()

    def open_product(self):
        return self.find_element(*LandingPageLoc.LNK_OPEN_PRODUCT).click()


class CartElement(BaseElement):

    def get_product_quantity(self) -> int:
        quantity = self.find_element(*CartItemsLoc.ITEM_QUANTITY).text
        return int(quantity)

    def get_product_name(self) -> str:
        return self.find_element(*CartItemsLoc.LNK_OPEN_PRODUCT).text

    def get_product_price(self) -> float:
        price = self.find_element(*CartItemsLoc.TXT_PRODUCT_PRICE).text.replace("$", "")
        return float(price)

    def remove_cart_item(self):
        return self.find_element(*CartItemsLoc.BTN_REMOVE).click()
