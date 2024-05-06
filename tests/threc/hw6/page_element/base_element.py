from tests.threc.hw6.locators import LocCheckoutPage, LocProductsPage, LocCartPage, LocFillForm
from tests.threc.hw6.page_object.base_page import BasePage


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


class CartElement(BaseElement, BasePage):
    def get_product_name(self) -> str:
        # get added to cart product name
        return self.text(self.find_element(*LocCartPage.cartProductName))


class CheckoutElement(BaseElement, BasePage):
    def find_and_get_product_label(self) -> str:
        # find product name and get this name
        return self.text(self.find_element(*LocCheckoutPage.checkoutItem))


class ProductElement(BaseElement, BasePage):
    def find_and_get_product_name(self, product) -> str:
        # Find and get product label
        return self.text(product.find_element(*LocProductsPage.productTitle))


class ProductDetailsElement(BasePage, BaseElement):
    def get_product_name(self) -> str:
        # Get product name
        return self.text(self.find_element(*LocProductsPage.productDetailsPage))


class FinishElement(BaseElement, BasePage):
    def get_finish_order_title(self) -> str:
        # find on the finish page title and get this title
        return self.text(self.find_element(*LocFillForm.finishOrderTitle))
