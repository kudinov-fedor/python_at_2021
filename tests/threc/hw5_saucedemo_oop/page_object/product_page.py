from tests.threc.hw5_saucedemo_oop.page_object.base_page import BasePage
from tests.threc.hw5_saucedemo_oop.locators import LocProductsPage


class ProductPage(BasePage):
    def list_products(self):
        products = self.find_elems(*LocProductsPage.listProducts)
        return products

    def line_product(self, index: int):
        one_product = self.list_products()[index]
        return one_product


    def product_label(self, product):
        label = product.find_element(*LocProductsPage.btnProductDetails)
        return label.text

    def product_details(self, product):
        product_details_btn = product.find_element(*LocProductsPage.btnProductDetails)
        return product_details_btn
