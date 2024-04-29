from tests.yana_pokulita.HW4_DemoQA.page.base_page import BasePage
from tests.yana_pokulita.locators import LoginPageLocators
from tests.yana_pokulita.HW4_DemoQA.page import constants


class LoginPage(BasePage):

    def open(self):
        self.driver.get(constants.HOST)

    def fill_form(self, login, password):
        self.driver.find_element(*LoginPageLocators.UserName).send_keys(login)
        self.driver.find_element(*LoginPageLocators.Password).send_keys(password)
        self.driver.find_element(*LoginPageLocators.LoginBtn).click()
