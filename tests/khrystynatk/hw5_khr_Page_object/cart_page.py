from tests.khrystynatk.hw5_khr_Page_object.base_page import BasePage
from tests.khrystynatk.hw5_khr_Page_object.locators1 import CartItemsLoc
from selenium.common import NoSuchElementException


class CartPage(BasePage):

    def remove_cart_item(self, index):
        items = self.driver.find_elements(*CartItemsLoc.CART_ITEMS)
        items[index].find_element(*CartItemsLoc.BTN_REMOVE).click()

    def get_cart_badge(self):
        cart = self.driver.find_element(*CartItemsLoc.CART_CONTAINER)
        try:
            cart.find_element(*CartItemsLoc.IMG_CART_BADGE).is_displayed()
        except NoSuchElementException:
            return 0
        return 1
