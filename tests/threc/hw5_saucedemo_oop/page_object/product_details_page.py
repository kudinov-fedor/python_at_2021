from tests.threc.hw5_saucedemo_oop.page_object.base_page import BasePage
from tests.threc.hw5_saucedemo_oop.locators import LocProductsPage


class ProductDetailsPage(BasePage):
    def get_product_name(self):
        # Get product name
        return self.text(*LocProductsPage.productDetailsPage)
