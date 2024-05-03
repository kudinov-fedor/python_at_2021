from tests.threc.hw5_saucedemo_oop import constants
from tests.threc.hw5_saucedemo_oop.page_object.base_page import BasePage
from tests.threc.hw5_saucedemo_oop.locators import LocSignupPage


class LoginPage(BasePage):
    def open(self):
        # open url
        self.driver.get(constants.URL_HOST)

    def fill_form(self, login: str, password: str):
        # fill login form with login and password
        self.find_element(*LocSignupPage.login).send_keys(login)
        self.find_element(*LocSignupPage.password).send_keys(password)

    def submit_login_form(self):
        # click on the login btn
        self.click(self.find_element(*LocSignupPage.btnLogin))
