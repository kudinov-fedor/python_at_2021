from tests.innahoncharenko.homework_5.pages.base_page import BasePage
from tests.innahoncharenko.homework_5.pages.landing_page import LandingPage
from tests.innahoncharenko.homework_5.pages.locators import LoginPageLocators


class LoginPage(BasePage):
    # Will return landing page
    def login(self, user_name, user_pass):

        self.find_element(LoginPageLocators.USER_NAME_FIELD).send_keys(user_name)
        self.find_element(LoginPageLocators.USER_PASS_FIELD).send_keys(user_pass)

        self.click_element(LoginPageLocators.SUBMIT_LOGIN_BUTTON)

        return LandingPage(self.driver)
