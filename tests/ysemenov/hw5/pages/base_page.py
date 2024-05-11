from selenium.webdriver.remote.webelement import WebElement
from tests.ysemenov.hw5.conftest import HOST
from tests.ysemenov.hw5.locators import LocatorsHeaderMenu
from selenium.common import NoSuchElementException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(HOST)

    def find_element(self, by: str, locator: str) -> WebElement:
        return self.driver.find_element(by, locator)

    def find_elements(self, by: str, locator: str) -> list[WebElement]:
        return self.driver.find_elements(by, locator)

    def send_keys(self, by: str, locator: str, text: str):
        self.find_element(by, locator).send_keys(text)

    def click_by_locator(self, by: str, locator: str):
        self.driver.find_element(by, locator).click()

    def click_cart_button(self):
        cart = self.driver.find_element(*LocatorsHeaderMenu.BTN_CART)
        cart.click()

    def get_cart_badge_number(self) -> int:
        try:
            cart = self.find_element(*LocatorsHeaderMenu.BTN_CART)
            cart_badge = cart.find_element(*LocatorsHeaderMenu.CART_BADGE)
            return int(cart_badge.text)
        except NoSuchElementException:
            return 0
