from tests.innahoncharenko.homework_6.pages.base_page import BasePage
from tests.innahoncharenko.homework_6.pages.landing_page import LandingPage
from tests.innahoncharenko.homework_6.pages.locators import LoginPageLocators
from typing import Self


class LoginPage(BasePage):
    def set_user_name(self, user_name) -> Self:
        self.find_element(LoginPageLocators.USER_NAME_FIELD).send_keys(user_name)
        return self

    def set_password(self, user_pass) -> Self:
        self.find_element(LoginPageLocators.USER_PASS_FIELD).send_keys(user_pass)
        return self

    def submit(self) -> LandingPage:
        self.click_element(LoginPageLocators.SUBMIT_LOGIN_BUTTON)
        return LandingPage(self.driver)
