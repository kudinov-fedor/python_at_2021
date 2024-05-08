from selenium.common import NoSuchElementException
from tests.threc.hw6.page_object.base_page import BasePage
from tests.threc.hw6.page_element.base_element import ProductDetailsElement
from tests.threc.hw6.locators import LocProductsPage
from tests.threc.hw6.page_element.base_element import BaseElement


class ProductPage(BasePage, BaseElement):
    def get_list_products(self):
        # List of products
        products = self.find_elements(*LocProductsPage.listProducts)
        return products

    def link_to_product_details(self, product) -> ProductDetailsElement:
        # navigate to the product details page
        self.click(product.find_element(*LocProductsPage.productTitle))
        return ProductDetailsElement(self.driver)

    def add_product_to_cart(self, index):
        # Add product to cart
        self.click(self.get_list_products()[index].find_element(*LocProductsPage.btnAddToCart))
        return self

    def get_badge_value(self) -> int:
        """Returns the value displayed on the cart badge."""
        try:
            cart_badge = self.find_element(*LocProductsPage.cartBadgeProduct).text
            return int(cart_badge)
        except NoSuchElementException:
            return 0
