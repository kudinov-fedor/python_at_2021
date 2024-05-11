from tests.yspryn.test_HW6.pages.base_page import BasePage
from tests.yspryn.test_HW6.pages import locators
from tests.yspryn.test_HW6.pages.base_elements import CartElement


class CartPage(BasePage):
    def list_of_products_in_cart(self) -> list[CartElement]:
        products_in_cart = self.find_elements(*locators.CartPage.TABLE_ITEMS_IN_CART)
        return [CartElement(el) for el in products_in_cart]
