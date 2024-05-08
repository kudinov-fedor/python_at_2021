from tests.threc.hw6.page_object.base_page import BasePage
from tests.threc.hw6.locators import LocCartPage


class CartPage(BasePage):

    def open_cart(self):
        # open cart page
        return self.click(self.find_element(*LocCartPage.cartLink))
