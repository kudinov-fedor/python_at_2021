from tests.ysemenov.hw5.pages.base_page import BasePage
from tests.ysemenov.hw5.locators import LocatorsProductDetailsPage


class ProductDetailsPage(BasePage):

    def add_to_cart(self):
        self.click_by_locator(*LocatorsProductDetailsPage.BTN_ADD_TO_CART)

    def remove_from_cart(self):
        self.click_by_locator(*LocatorsProductDetailsPage.BTN_REMOVE)

    def back_to_products(self):
        self.click_by_locator(*LocatorsProductDetailsPage.BTN_BACK_TO_PRODUCTS)
