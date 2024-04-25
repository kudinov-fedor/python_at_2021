from tests.khrystynatk.hw5_khr_Page_object.base_page import BasePage
from tests.khrystynatk.hw5_khr_Page_object.locators1 import LandingPageLoc, CartItemsLoc


class CartPage(BasePage):

    def open_landing_page(self):
        self.open_page()
        self.input_creds(self.USERNAME, self.PASSWORD)

    def add_items(self):
        elements = self.driver.find_elements(*LandingPageLoc.LST_ITEMS)
        elements[0].find_element(*LandingPageLoc.BTN_ADD_TO_CART).click()
        elements[1].find_element(*LandingPageLoc.BTN_ADD_TO_CART).click()
        elements[2].find_element(*LandingPageLoc.BTN_ADD_TO_CART).click()

    def move_to_cart(self):
        cart_link = self.driver.find_element(*LandingPageLoc.LNK_CART)
        cart_link.click()

    def remove_cart_items(self):
        items = self.driver.find_elements(*CartItemsLoc.CART_ITEMS)
        items[0].find_element(*CartItemsLoc.BTN_REMOVE_FIRST).click()
        items[1].find_element(*CartItemsLoc.BTN_REMOVE_SECOND).click()
        items[2].find_element(*CartItemsLoc.BTN_REMOVE_THIRD).click()

    def cart_container(self):
        cart = self.driver.find_element(*CartItemsLoc.CART_CONTAINER)
        cart.find_element(*CartItemsLoc.IMG_CART_BADGE)
