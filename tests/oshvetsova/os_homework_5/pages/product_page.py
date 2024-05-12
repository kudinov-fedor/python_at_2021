from .base_page import BasePage
from .locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    def find_products(self) -> list:
        elements = self.driver.find_elements(*ProductPageLocator.PRODUCT_LIST)
        return elements

    def add_to_cart(self, index):
        self.find_products()[index].find_element(*ProductPageLocator.BTN_ADD_TO_CART).click()

    def open_cart(self):
        cart_link = self.driver.find_element(*ShoppingCart.LNK_CART)
        cart_link.click()

    def logout_from_system(self):
        self.driver.find_element(*SideNavigation.BTN_NAVIGATION_MENU).click()
        wait = WebDriverWait(self.driver, 2)
        logout_button = wait.until(EC.element_to_be_clickable(SideNavigation.LOGOUT_BUTTON))
        logout_button.click()

