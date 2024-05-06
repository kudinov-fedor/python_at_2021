from tests.yspryn.test_HW5.pages.base_page import BasePage
from tests.yspryn.test_HW5.pages import locators


class CartPage(BasePage):

    def get_number_of_products_in_cart(self) -> int:
        products_in_cart = self.find_elements(*locators.CartPage.TABLE_ITEMS_IN_CART)
        return len(products_in_cart)

    def get_list_of_products_in_cart(self) -> list:
        return self.find_elements(*locators.CartPage.TABLE_ITEMS_IN_CART)

    def remove_item_from_cart(self, index: int):
        list_of_products = self.get_list_of_products_in_cart()
        list_of_products[index].find_element(*locators.CartPage.BTN_REMOVE_FROM_CART).click()
