from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from .base_element import PageElement
from .locators import SideNavigation


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self, host: str) -> None:
        self.driver.get(host)

    def get_url(self) -> str:
        return self.driver.current_url

    def find_elements(self, by, value) -> list[PageElement]:
        return [PageElement(el) for el in self.driver.find_elements(by, value)]

    def find_element(self, by: str, locator: str) -> 'PageElement':
        return PageElement(self.driver.find_element(by, locator))

    def get_side_navigation(self) -> WebElement:
        return self.driver.find_element(*SideNavigation.BTN_NAVIGATION_MENU)
