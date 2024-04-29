from tests.threc.hw5_saucedemo_oop.page_object.base_page import BasePage
from tests.threc.hw5_saucedemo_oop.locators import LocProductsPage


class ProductDetailsPage(BasePage):
    def product_details_label(self):
        label = self.driver.find_element(*LocProductsPage.productDetailsPage)
        return label.text
