from tests.vvashchu.pages.base_page import BasePage
from tests.vvashchu.pages.products_page import ProductsPage
from tests.vvashchu.locators import LoginPageLocators
from tests.vvashchu import constants


class LoginPage(BasePage):

    def open(self):
        self.driver.get(constants.HOST)
        return self

    def fill_form(self, login, password):
        self.driver.find_element(*LoginPageLocators.UserName).send_keys(login)
        self.driver.find_element(*LoginPageLocators.Password).send_keys(password)
        self.click(*LoginPageLocators.LoginBtn)
        return ProductsPage(self.driver)
