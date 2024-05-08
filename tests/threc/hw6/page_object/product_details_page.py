from tests.threc.hw6.page_object.base_page import BasePage
from tests.threc.hw6.locators import LocProductsPage


class ProductDetailsPage(BasePage):
    def get_product_name(self) -> str:
        # Get product name
        return self.text(self.find_element(*LocProductsPage.productDetailsPage))
