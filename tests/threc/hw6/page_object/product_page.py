from typing import List
from selenium.common import NoSuchElementException
from tests.threc.hw6.page_element.base_element import BaseElement, ProductElement
from tests.threc.hw6.locators import LocProductsPage


class ProductPage(BaseElement):
    def get_list_products(self) -> List[ProductElement]:
        # List of products
        products = []
        for p in self.find_elements(*LocProductsPage.listProducts):
            products.append(ProductElement(p))
        return products

    def get_badge_value(self) -> int:
        """Returns the value displayed on the cart badge."""
        try:
            cart_badge = self.find_element(*LocProductsPage.cartBadgeProduct).text
            return int(cart_badge)
        except NoSuchElementException:
            return 0
