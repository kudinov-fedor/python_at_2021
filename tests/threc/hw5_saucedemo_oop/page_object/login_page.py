from tests.threc.hw5_saucedemo_oop import constants
from tests.threc.hw5_saucedemo_oop.page_object.base_page import BasePage
from tests.threc.hw5_saucedemo_oop.locators import LocSignupPage


class LoginPage(BasePage):
    def open(self):
        self.driver.get(constants.URL_HOST)

    def fill_form(self, login: str, password: str):
        self.find_elem(*LocSignupPage.login).send_keys(login)
        self.find_elem(*LocSignupPage.password).send_keys(password)

    def submit_btn(self):
        btn = self.find_elem(*LocSignupPage.btnLogin)
        return btn
