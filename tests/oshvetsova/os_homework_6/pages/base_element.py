from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.oshvetsova.os_homework_6.pages.locators import SideNavigation


class PageElement:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, by, value) -> WebElement:
        return self.driver.find_element(by, value)

    def find_elements(self, by, value) -> list[WebElement]:
        return self.driver.find_elements(by, value)

    def __getattr__(self, item):
        try:
            return self.__dict__[item]
        except KeyError:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{item}'")


class SideNavigationElement(PageElement):
    def open_navigation_menu(self):
        self.driver.find_element(*SideNavigation.BTN_NAVIGATION_MENU).click()

    def click_logout_button(self):
        wait = WebDriverWait(self.driver, 2)
        logout_button = wait.until(EC.element_to_be_clickable(SideNavigation.LOGOUT_BUTTON))
        logout_button.click()
