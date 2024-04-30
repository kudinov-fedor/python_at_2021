from tests.yspryn.test_HW5.pages.base_page import BasePage
from tests.yspryn.test_HW5.pages import locators


class LoginPage(BasePage):

    def fill_login_form(self, login, password):
        self.find_element(*locators.LoginPage.TXT_LOGIN_INPUT).send_keys(login)
        self.find_element(*locators.LoginPage.TXT_PASSWORD_INPUT).send_keys(password)
        self.find_element(*locators.LoginPage.BTN_SUBMIT).click()
