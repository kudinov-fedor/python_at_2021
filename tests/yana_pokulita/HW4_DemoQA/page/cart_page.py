from tests.yana_pokulita.HW4_DemoQA.page.base_page import BasePage
from tests.yana_pokulita.locators import CartLocators


class CartPage(BasePage):
    def cart_elements(self):
        cart_elements = self.driver.find_elements(*CartLocators.ShoppingCart)
        return cart_elements

    def cart_badge(self):
        cart_badge = self.driver.find_element(*CartLocators.ShoppingCartBadge)
        return cart_badge

    def go_to_cart(self):
        self.driver.find_element(*CartLocators.ShoppingCart).click()

    def get_cart_items(self):
        cart_items = self.driver.find_elements(*CartLocators.CartItems)
        return cart_items

    def go_to_checkout(self):
        self.driver.find_element(*CartLocators.CheckOutBtn).click()

    def remove_cart_item(self,index):
        items = self.driver.find_elements(*CartLocators.CartItems)
        items[index].find_element(*CartLocators.RemoveItemBtn).click()

    def checkout_btn_status(self):
        checkout_btn = self.driver.find_element(*CartLocators.CheckOutBtn).is_enabled()
        return checkout_btn
