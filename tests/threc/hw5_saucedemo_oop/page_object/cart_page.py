from tests.threc.hw5_saucedemo_oop.page_object.base_page import BasePage
from tests.threc.hw5_saucedemo_oop.locators import LocCartPage
from tests.threc.hw5_saucedemo_oop.locators import LocCheckoutPage


class CartPage(BasePage):
    def shopping_cart_badge(self):
        cart = self.driver.find_element(*LocCartPage.shoppingCart)
        cart_badge = cart.find_element(*LocCartPage.cartBadge)
        return cart_badge

    def cart_badge_label(self, cart_badge):
        name = cart_badge.text
        return name

    def cart_product_name(self):
        label = self.driver.find_element(*LocCartPage.cartProductName)
        return label.text

    def cart_continue_btn(self):
        continue_btn = self.driver.find_element(*LocCheckoutPage.btnContinueShopping)
        return continue_btn

    def cart_checkout_btn(self):
        checkout_btn = self.driver.find_element(*LocCheckoutPage.btnCheckout)
        return checkout_btn

    def btn_click(self, button):
        button.click()
