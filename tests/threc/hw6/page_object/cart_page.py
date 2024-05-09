from typing import List

from tests.threc.hw6.page_object.base_page import BasePage
from tests.threc.hw6.page_object.checkout_page import CheckoutPage
from tests.threc.hw6.locators import LocCheckoutPage, LocCartPage
from tests.threc.hw6.page_element.base_element import CartElement


class CartPage(BasePage):
    def click_continue_btn(self):
        # find button continue and click it
        self.click(self.find_element(*LocCheckoutPage.btnContinueShopping))

    def click_checkout_btn(self) -> CheckoutPage:
        # find button checkout and click it
        self.click(self.find_element(*LocCheckoutPage.btnCheckout))
        return CheckoutPage(self.driver)

    def get_products(self) -> List[CartElement]:
        # List of added products to the cart
        added_products = []
        for p in self.find_elements(*LocCartPage.cartAddedProducts):
            added_products.append(CartElement(p))
        return added_products
