from tests.yana_pokulita.HW4_DemoQA.page.base_page import BasePage
from tests.yana_pokulita.locators import ProductPageLocators


class ProductsPage(BasePage):
    def get_elements(self):
        elements = self.driver.find_elements(*ProductPageLocators.Elements)
        return elements

    def move_to_cart(self, index):
        self.get_elements()[index].find_element(*ProductPageLocators.Element).click()

