from tests.ysemenov.hw5.pages.base_page import BasePage
from tests.ysemenov.hw5.locators import LocatorsInventoryPage


class InventoryPage(BasePage):

    def get_products(self):
        return self.find_elements(*LocatorsInventoryPage.LST_INVENTORY)

    # def add_product_to_cart(self, position: int):
    #     elements = self.find_elements(*LocatorsInventoryPage.LST_INVENTORY)
    #     elements[position].find_element(*LocatorsInventoryPage.BTN_ADD_TO_CART).click()

    def add_product_to_cart(self, product):
        product.find_element(*LocatorsInventoryPage.BTN_ADD_TO_CART).click()

    # def open_product_page(self, position: int):
    #     elements = self.find_elements(*LocatorsInventoryPage.LST_INVENTORY)
    #     product_name_link = elements[position].find_element(*LocatorsInventoryPage.LNK_PRODUCT_NAME)
    #     product_name_link.click()

    def open_product_page(self, product):
        product.find_element(*LocatorsInventoryPage.LNK_PRODUCT_NAME).click()
