from tests.threc.hw5_saucedemo_oop.page_object.base_page import BasePage
from tests.threc.hw5_saucedemo_oop.locators import LocProductsPage


class ProductPage(BasePage):
    def get_list_products(self):
        # List of products
        return self.find_elements(*LocProductsPage.listProducts)

    def add_product_to_cart(self, index):
        # Add product to cart
        self.click(self.get_list_products()[index].find_element(*LocProductsPage.btnAddToCart))

    def find_and_get_product_label(self, index):
        # Find and get product label
        return self.get_list_products()[index].find_element(*LocProductsPage.btnProductDetails).text

    def link_to_product_details(self):
        # navigate to the product details page
        self.click(self.find_element(*LocProductsPage.btnProductDetails))
