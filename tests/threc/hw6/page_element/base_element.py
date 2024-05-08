from tests.threc.hw6.locators import LocProductsPage, LocCartPage, LocFillForm, LocCheckoutPage
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from tests.threc.hw6.page_object.product_details_page import ProductDetailsPage
from tests.threc.hw6.page_object.finish_page import FinishPage
from tests.threc.hw6.page_object.checkout_page import CheckoutPage


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
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()
        except TimeoutException:
            raise AssertionError(f"Timed out waiting for element to be clickable: {locator}")


class CartElement(BaseElement):
    def get_name(self) -> str:
        # get added to cart product name
        return self.text(self.find_element(*LocCartPage.cartProductName))

    def click_continue_btn(self):
        # find button continue and click it
        self.click(self.find_element(*LocCheckoutPage.btnContinueShopping))

    def click_checkout_btn(self) -> CheckoutPage:
        # find button checkout and click it
        self.click(self.find_element(*LocCheckoutPage.btnCheckout))
        return CheckoutPage(self.driver)


class CheckoutElement(BaseElement):
    def get_label(self) -> str:
        # find product name and get this name
        return self.text(self.find_element(*LocCheckoutPage.checkoutItem))

    def click_submit_btn(self):
        # submit checkout form
        self.click(self.find_element(*LocFillForm.btnContinue))
        return self

    def click_finish_btn(self) -> FinishPage:
        # find finish button and click it
        self.click(self.find_element(*LocFillForm.btnFinish))
        return FinishPage(self.driver)


class ProductElement(BaseElement):
    """
    продукт один та операція над продуктом
    сутність цього інстансу - це продукт який в ньому знаходиться
    """
    def get_name(self) -> str:
        # Find and get product label
        return self.text(self.find_element(*LocProductsPage.productTitle))

    def add_product_to_cart(self):
        # Add product to cart
        self.click(self.find_element(*LocProductsPage.btnAddToCart))
        return self

    def link_to_product_details(self) -> ProductDetailsPage:
        # navigate to the product details page
        self.click(self.find_element(*LocProductsPage.productTitle))
        return ProductDetailsPage(self.driver)

    def get_badge_value(self) -> int:
        # Returns the value displayed on the cart badge
        try:
            cart_badge = self.find_element(*LocProductsPage.cartBadgeProduct).text
            return int(cart_badge)
        except NoSuchElementException:
            return 0
