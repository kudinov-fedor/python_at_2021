from selenium.webdriver.remote.webelement import WebElement
from selenium.common import NoSuchElementException
from tests.ysemenov.hw6.constants import HOST
from tests.ysemenov.hw6.locators import LocatorsHeaderMenu


class BaseElement:

    def __init__(self, element: WebElement):
        self.element = element

    def send_keys(self, text: str):
        self.element.send_keys(text)

    def click(self):
        self.element.click()

    def find_element(self, by: str, locator: str) -> 'BaseElement':
        return BaseElement(self.element.find_element(by, locator))

    @property
    def text(self) -> str:
        return self.element.text


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(HOST)
        return self

    def find_element(self, by: str, locator: str) -> BaseElement:
        return BaseElement(self.driver.find_element(by, locator))

    def find_elements(self, by: str, locator: str) -> list[BaseElement]:
        web_elements = self.driver.find_elements(by, locator)
        return [BaseElement(element) for element in web_elements]

    def send_keys(self, by: str, locator: str, text: str):
        self.find_element(by, locator).send_keys(text)

    def click_by_locator(self, by: str, locator: str):
        self.find_element(by, locator).click()

    def click_cart_button(self):
        from tests.ysemenov.hw6.pages import CartPage
        cart = self.find_element(*LocatorsHeaderMenu.BTN_CART)
        cart.click()
        return CartPage(self.driver)

    @property
    def cart_badge_num(self) -> int:
        try:
            cart = self.find_element(*LocatorsHeaderMenu.BTN_CART)
            cart_badge = cart.find_element(*LocatorsHeaderMenu.CART_BADGE)
            return int(cart_badge.text)
        except NoSuchElementException:
            return 0
