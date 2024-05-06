from tests.threc.hw6 import constants
from tests.threc.hw6.page_object.base_page import BasePage
from tests.threc.hw6.page_element.base_element import BaseElement
from tests.threc.hw6.page_object.product_page import ProductPage
from tests.threc.hw6.locators import LocSignupPage


class LoginPage(BasePage, BaseElement):
    def open(self):
        # open url
        self.driver.get(constants.URL_HOST)
        return self

    def fill_form(self, login: str, password: str):
        # fill login form with login and password
        self.find_element(*LocSignupPage.login).send_keys(login)
        self.find_element(*LocSignupPage.password).send_keys(password)
        return self

    def submit_login_form(self):
        # click on the login btn
        self.click(self.find_element(*LocSignupPage.btnLogin))
        return ProductPage(self.driver)
