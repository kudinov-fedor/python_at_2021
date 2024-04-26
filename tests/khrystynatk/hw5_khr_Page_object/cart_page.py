from tests.khrystynatk.hw5_khr_Page_object.base_page import BasePage
from tests.khrystynatk.hw5_khr_Page_object.locators1 import CartItemsLoc


class CartPage(BasePage):

    def remove_cart_items(self):
        items = self.driver.find_elements(*CartItemsLoc.CART_ITEMS)
        items[0].find_element(*CartItemsLoc.BTN_REMOVE_FIRST).click()
        items[1].find_element(*CartItemsLoc.BTN_REMOVE_SECOND).click()
        items[2].find_element(*CartItemsLoc.BTN_REMOVE_THIRD).click()

    def cart_container(self):
        cart = self.driver.find_element(*CartItemsLoc.CART_CONTAINER)
        cart.find_element(*CartItemsLoc.IMG_CART_BADGE)
