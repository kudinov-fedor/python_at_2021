from tests.khrystynatk.hw5_khr_Page_object.base_page import BasePage
from tests.khrystynatk.hw5_khr_Page_object.locators1 import LandingPageLoc, SideMenuLoc


class ItemsPage(BasePage):

    def find_product_rows(self):
        elements = self.driver.find_elements(*LandingPageLoc.LST_ITEMS)
        return elements

    def add_to_cart(self, index):
        self.find_product_rows()[index].find_element(*LandingPageLoc.BTN_ADD_TO_CART).click()

    def logout_from_side_menu(self):
        self.driver.find_element(*SideMenuLoc.BTN_BURGER_MENU).click()
        self.driver.find_element(*SideMenuLoc.LNK_LOGOUT).click()

    def go_to_cart(self):
        cart_link = self.driver.find_element(*LandingPageLoc.LNK_CART)
        cart_link.click()
