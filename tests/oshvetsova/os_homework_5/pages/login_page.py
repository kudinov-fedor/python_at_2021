from tests.oshvetsova.os_homework_5.pages.base_page import BasePage
from tests.oshvetsova.os_homework_5.pages.locators import LogInPageLoc
from selenium.webdriver.remote.webelement import WebElement


class LogInPage(BasePage):

    def find_username_field(self) -> WebElement:
        return self.driver.find_element(*LogInPageLoc.USER_NAME)

    def find_password_field(self) -> WebElement:
        return self.driver.find_element(*LogInPageLoc.PASSWORD)

    def input_creds(self, username, password):
        self.find_username_field().send_keys(username)
        self.find_password_field().send_keys(password)
        self.driver.find_element(*LogInPageLoc.BTN_LOGIN).click()
