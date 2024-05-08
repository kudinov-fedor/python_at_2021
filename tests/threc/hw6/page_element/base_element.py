from tests.threc.hw6.locators import LocCheckoutPage, LocProductsPage, LocCartPage, LocFillForm
from tests.threc.hw6.page_object.base_page import BasePage
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:
    def __init__(self, driver):
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
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            raise AssertionError(f"Timed out waiting for element to be clickable: {locator}")


class CartElement(BaseElement):
    def get_product_name(self) -> str:
        # get added to cart product name
        return self.text(self.find_element(*LocCartPage.cartProductName))


class CheckoutElement(BaseElement, BasePage):
    def find_and_get_product_label(self) -> str:
        # find product name and get this name
        return self.text(self.find_element(*LocCheckoutPage.checkoutItem))


class ProductElement(BaseElement):
    def find_and_get_product_name(self, product) -> str:
        # Find and get product label
        return self.text(product.find_element(*LocProductsPage.productTitle))


class ProductDetailsElement(BaseElement):
    def get_product_name(self) -> str:
        # Get product name
        return self.text(self.find_element(*LocProductsPage.productDetailsPage))


class FinishElement(BaseElement):
    def get_finish_order_title(self) -> str:
        # find on the finish page title and get this title
        return self.text(self.find_element(*LocFillForm.finishOrderTitle))
