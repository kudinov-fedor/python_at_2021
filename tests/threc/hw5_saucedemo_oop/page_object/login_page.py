from tests.threc.hw5_saucedemo_oop import constants
from tests.threc.hw5_saucedemo_oop.page_object.base_page import BasePage
from tests.threc.hw5_saucedemo_oop.locators import SignupPage


class LoginPage(BasePage):
    def open(self):
        self.driver.get(constants.URL_HOST)

    def fill_form(self, login, password):
        self.driver.find_element(*SignupPage.login).send_keys(login)
        self.driver.find_element(*SignupPage.password).send_keys(password)

    def submit(self):
        self.driver.find_element(*SignupPage.btnLogin).click()