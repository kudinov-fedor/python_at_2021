from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.oshvetsova.os_homework_6.pages.locators import SideNavigation


class PageElement:
    def __init__(self, driver: WebElement):
        self.driver = driver

    def find_element(self, by: str, locator: str) -> 'PageElement':
        return PageElement(self.driver.find_element(by, locator))

    def click(self):
        self.driver.click()

    def is_displayed(self) -> bool:
        return self.driver.is_displayed()

    @property
    def text(self) -> str:
        return self.driver.text


class SideNavigationElement(PageElement):
    def get_side_navigation(self):
        return self.driver.find_element(*SideNavigation.BTN_NAVIGATION_MENU)

    def click_logout_button(self):
        wait = WebDriverWait(self.driver, 2)
        logout_button = wait.until(EC.element_to_be_clickable(SideNavigation.LOGOUT_BUTTON))
        logout_button.click()
