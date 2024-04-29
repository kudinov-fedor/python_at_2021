from tests.mariana_petrushanska.test_selenium_hw4.base_page import BasePage
from tests.mariana_petrushanska.test_selenium_hw4.locators import LoginPageLoc


class LoginPage(BasePage):

    def fill_in_login_form(self, login, password):
        self.driver.find_element(*LoginPageLoc.TXT_USERNAME).send_keys(login)
        self.driver.find_element(*LoginPageLoc.TXT_PASSWORD).send_keys(password)

    def confirm_login(self):
        self.driver.find_element(*LoginPageLoc.BTN_LOGIN).click()
