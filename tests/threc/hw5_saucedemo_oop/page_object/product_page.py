from selenium.common import NoSuchElementException

from tests.threc.hw5_saucedemo_oop.page_object.base_page import BasePage
from tests.threc.hw5_saucedemo_oop.locators import LocProductsPage, LocCartPage


class ProductPage(BasePage):
    def get_list_products(self):
        # List of products
        return self.find_elements(*LocProductsPage.listProducts)

    def add_product_to_cart(self, product):
        # Add product to cart
        self.click(product.find_element(*LocProductsPage.btnAddToCart))

    def find_and_get_first_product_name(self):
        # Find and get product label
        return self.text(*LocProductsPage.btnProductDetails)

    def link_to_first_product_details(self):
        # navigate to the product details page
        self.click(self.find_element(*LocProductsPage.btnProductDetails))

    def get_badge_value(self):
        try:
            # amount of added products from the data on the badge
            cart_badge = self.driver.find_element(*LocCartPage.cartBadge).text
        except NoSuchElementException:
            return 0
        return int(cart_badge)
