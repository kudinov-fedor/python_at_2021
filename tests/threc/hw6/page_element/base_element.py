from tests.threc.hw6.locators import LocProductsPage, LocCartPage, LocCheckoutPage
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from tests.threc.hw6.page_object.product_details_page import ProductDetailsPage


class BaseElement:
    def __init__(self, driver: WebElement):
        self.driver = driver

    @classmethod
    def text(cls, label):
        return label.text

    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_elements(self, by, locator):
        return self.driver.find_elements(by, locator)

    def click(self, locator, timeout=0):
        """Clicks an element with waiting for it to be clickable."""
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()
        except TimeoutException:
            raise AssertionError(f"Timed out waiting for element to be clickable: {locator}")


class CartElement(BaseElement):
    def get_name(self) -> str:
        # get added to cart product name
        return self.text(self.find_element(*LocCartPage.cartProductName))


class CheckoutElement(BaseElement):
    def get_label(self) -> str:
        # find product name and get this name
        return self.text(self.find_element(*LocCheckoutPage.checkoutItem))


class ProductElement(BaseElement):
    """
    продукт один та операція над продуктом
    сутність цього інстансу - це продукт який в ньому знаходиться
    """
    def get_name(self) -> str:
        # Find and get product label
        return self.text(self.find_element(*LocProductsPage.productTitle))

    def add_to_cart(self):
        # Add product to cart
        self.click(self.find_element(*LocProductsPage.btnAddToCart))
        return self

    def go_to_details(self) -> ProductDetailsPage:
        # navigate to the product details page
        self.click(self.find_element(*LocProductsPage.productTitle))
        return ProductDetailsPage(self.driver)
