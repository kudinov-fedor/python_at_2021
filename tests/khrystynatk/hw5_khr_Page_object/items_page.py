from tests.khrystynatk.hw5_khr_Page_object.base_page import BasePage
from tests.khrystynatk.hw5_khr_Page_object.locators1 import LandingPageLoc, SideMenuLoc


class ItemsPage(BasePage):

    def open_landing_page(self):
        self.open_page()
        self.input_creds(self.USERNAME, self.PASSWORD)

    def find_elements(self):
        elements = self.driver.find_elements(*LandingPageLoc.LST_ITEMS)
        return elements

    def add_to_cart(self):
        self.find_elements()[0].find_element(*LandingPageLoc.BTN_ADD_TO_CART).click()
        self.find_elements()[1].find_element(*LandingPageLoc.BTN_ADD_TO_CART).click()
        self.find_elements()[2].find_element(*LandingPageLoc.BTN_ADD_TO_CART).click()

    def logout_from_side_menu(self):
        self.driver.find_element(*SideMenuLoc.BTN_BURGER_MENU).click()
        self.driver.find_element(*SideMenuLoc.LNK_LOGOUT).click()
