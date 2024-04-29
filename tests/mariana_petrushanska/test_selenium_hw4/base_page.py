from tests.mariana_petrushanska.test_selenium_hw4 import constants
from tests.mariana_petrushanska.test_selenium_hw4.locators import CartItemsLoc


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(constants.HOST)

    def go_to_cart(self):
        self.driver.find_element(*CartItemsLoc.IMG_CART).click()

    def get_cart_badge_number(self):
        cart = self.driver.find_element(*CartItemsLoc.IMG_CART)
        try:
            cart_badge = cart.find_element(*CartItemsLoc.IMG_CART_BADGE)
        except NoSuchElementException:
            return 0
        return int(cart_badge.text)
