from tests.yana_pokulita.HW4_DemoQA.page.base_page import BasePage
from tests.yana_pokulita.locators import LoginPageLocators


class LoginPage(BasePage):

    def open(self):
        self.driver.get("https://www.saucedemo.com")

    def fill_form(self, login, password):
        self.driver.find_element(*LoginPageLocators.UserName).send_keys(login)
        self.driver.find_element(*LoginPageLocators.Password).send_keys(password)
        self.driver.find_element(*LoginPageLocators.LoginBtn).click()