from tests.khrystynatk.hw5_khr_Page_object.base_page import BasePage
from tests.khrystynatk.hw5_khr_Page_object.locators1 import CartItemsLoc


class CartPage(BasePage):

    def remove_cart_items(self, index):
        items = self.driver.find_elements(*CartItemsLoc.CART_ITEMS)
        items[index].find_element(*CartItemsLoc.BTN_REMOVE).click()

    def get_cart_badge(self):
        cart = self.driver.find_element(*CartItemsLoc.CART_CONTAINER)
        if not cart.find_element(*CartItemsLoc.IMG_CART_BADGE).is_displayed():
            return False
        return True
