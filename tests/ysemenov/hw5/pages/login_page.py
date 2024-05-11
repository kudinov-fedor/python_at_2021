from tests.ysemenov.hw5.pages.base_page import BasePage
from tests.ysemenov.hw5.locators import LocatorsLoginPage


class LoginPage(BasePage):

    def fill_login_form(self, login: str, password: str):
        self.send_keys(*LocatorsLoginPage.TXT_LOGIN, login)
        self.send_keys(*LocatorsLoginPage.TXT_PASSWORD, password)

    def submit_login_form(self):
        self.click_by_locator(*LocatorsLoginPage.BTN_SUBMIT)

    def log_in(self, login: str, password: str):
        self.fill_login_form(login, password)
        self.submit_login_form()
