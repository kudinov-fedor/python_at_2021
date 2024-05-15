from selenium.common import NoSuchElementException
from tests.mariana_petrushanska.test_selenium_hw5 import constants
from tests.mariana_petrushanska.test_selenium_hw5.locators import CartItemsLoc


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(constants.HOST)
        return self

    def find_elements(self, by, locator):
        return self.driver.find_elements(by, locator)

    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)

    def click(self, by, locator):
        self.find_element(by, locator).click()

    def go_to_cart(self):
        self.click(*CartItemsLoc.IMG_CART)

    def get_cart_badge_number(self) -> int:
        cart = self.find_element(*CartItemsLoc.IMG_CART)
        try:
            cart_badge = cart.find_element(*CartItemsLoc.IMG_CART_BADGE)
        except NoSuchElementException:
            return 0
        return int(cart_badge.text)
