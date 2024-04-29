from tests.yana_pokulita.HW4_DemoQA.page.base_page import BasePage
from tests.yana_pokulita.locators import ProductPageLocators


class ProductsPage(BasePage):
    def get_products(self):
        elements = self.driver.find_elements(*ProductPageLocators.Elements)
        return elements

    def move_product_to_cart(self, index):
        self.get_products()[index].find_element(*ProductPageLocators.Element).click()

