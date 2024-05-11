import pytest
from tests.ysemenov.hw5.conftest import HOST
from tests.ysemenov.hw5.locators import LocatorsHeaderMenu
from selenium.common import NoSuchElementException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(HOST)

    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_elements(self, by, locator):
        return self.driver.find_elements(by, locator)

    def send_keys(self, by, locator, text):
        self.find_element(by, locator).send_keys(text)

    def click_by_locator(self, by, locator):
        self.driver.find_element(by, locator).click()

    def click_cart_button(self):
        cart = self.driver.find_element(*LocatorsHeaderMenu.BTN_CART)
        cart.click()

    # def check_cart_badge_number(self, number):
    #     cart = self.find_element(*LocatorsHeaderMenu.BTN_CART)
    #     cart_badge = cart.find_element(*LocatorsHeaderMenu.CART_BADGE)
    #     assert cart_badge.text == number
    #
    # def check_cart_badge_empty(self):
    #     cart = self.find_element(*LocatorsHeaderMenu.BTN_CART)
    #
    #     with pytest.raises(NoSuchElementException):
    #         cart.find_element(*LocatorsHeaderMenu.CART_BADGE)

    def get_cart_badge_number(self):
        try:
            cart = self.find_element(*LocatorsHeaderMenu.BTN_CART)
            cart_badge = cart.find_element(*LocatorsHeaderMenu.CART_BADGE)
            return int(cart_badge.text)
        except NoSuchElementException:
            return 0
