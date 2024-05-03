from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from tests.threc.hw5_saucedemo_oop.page_object.base_page import BasePage
from tests.threc.hw5_saucedemo_oop.locators import LocProductsPage, LocCartPage


class ProductPage(BasePage):
    def get_list_products(self):
        # List of products
        return self.find_elements(*LocProductsPage.listProducts)

    def add_product_to_cart(self, product: WebElement):
        # Add product to cart
        self.click(product.find_element(*LocProductsPage.btnAddToCart))

    def find_and_get_product_name(self, product):
        # Find and get product label
        # self.text(product.find_element(*LocProductsPage.btnProductDetails))
        return self.text(product.find_element(*LocProductsPage.productTitle))

    def link_to_product_details(self, product):
        # navigate to the product details page
        self.click(product.find_element(*LocProductsPage.productTitle))

    def get_badge_value(self):
        try:
            # amount of added products from the data on the badge
            cart_badge = self.driver.find_element(*LocCartPage.cartBadge).text
        except NoSuchElementException:
            return 0
        return int(cart_badge)
