from tests.oshvetsova.os_homework_5.pages.base_page import BasePage
from tests.oshvetsova.os_homework_5.pages.locators import LogInPageLoc


class LogInPage(BasePage):

    def input_creds(self, username, password):
        self.driver.find_element(*LogInPageLoc.USER_NAME).send_keys(username)
        self.driver.find_element(*LogInPageLoc.PASSWORD).send_keys(password)
        self.driver.find_element(*LogInPageLoc.BTN_LOGIN).click()

    def find_username_field(self):
        return self.driver.find_element(*LogInPage.USER_NAME)

    def find_password_field(self):
        return self.driver.find_element(*LogInPage.PASSWORD)
