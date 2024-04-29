from tests.threc.hw5_saucedemo_oop.page_object.base_page import BasePage
from tests.threc.hw5_saucedemo_oop.locators import LocProductsPage


class ProductPage(BasePage):
    def list_products(self):
        products = self.driver.find_elements(*LocProductsPage.listProducts)
        return products

    # def line_product(self, products, index):
    #     one_product = products[index].find_element(*LocProductsPage.btnAddToCart)
    #     return one_product


    def line_product(self, index):
        one_product = self.list_products()[index]
        return one_product


    # def add_cart(self, product):
    #     product.click()


    def add_to_cart(self, product):
        product.find_element(*LocProductsPage.btnAddToCart).click()


    def product_label(self, product):
        label = product.find_element(*LocProductsPage.btnProductDetails)
        return label.text


    def product_details(self, product):
        details = product.find_element(*LocProductsPage.btnProductDetails)
        details.click()
