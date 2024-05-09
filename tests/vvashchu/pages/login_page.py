from tests.vvashchu.pages.base_page import BasePage
from tests.vvashchu.locators import LoginPageLocators
from tests.vvashchu import constants


class LoginPage(BasePage):

    def open(self):
        self.driver.get(constants.HOST)

    def fill_form(self, login, password):
        self.driver.find_element(*LoginPageLocators.UserName).send_keys(login)
        self.driver.find_element(*LoginPageLocators.Password).send_keys(password)
        self.click(*LoginPageLocators.LoginBtn)
