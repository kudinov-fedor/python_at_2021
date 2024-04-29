from tests.threc.hw5_saucedemo_oop.page_object.base_page import BasePage
from tests.threc.hw5_saucedemo_oop.locators import LocCartPage
from tests.threc.hw5_saucedemo_oop.locators import LocCheckoutPage


class CartPage(BasePage):
    def shopping_cart_badge(self):
        cart = self.find_elem(*LocCartPage.shoppingCart)
        cart_badge = cart.find_element(*LocCartPage.cartBadge)
        return cart_badge

    def cart_badge_label(self, cart_badge):
        label = cart_badge.text
        return label

    def cart_product_name(self):
        name = self.find_elem(*LocCartPage.cartProductName)
        return name.text

    def cart_continue_btn(self):
        continue_btn = self.find_elem(*LocCheckoutPage.btnContinueShopping)
        return continue_btn

    def cart_checkout_btn(self):
        checkout_btn = self.find_elem(*LocCheckoutPage.btnCheckout)
        return checkout_btn
