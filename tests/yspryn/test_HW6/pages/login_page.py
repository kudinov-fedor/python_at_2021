from tests.yspryn.test_HW6.pages.base_page import BasePage
from tests.yspryn.test_HW6.pages import locators


class LoginPage(BasePage):

    def fill_login_form(self, login: str, password: str):
        """
        fill in form
        """
        self.find_element(*locators.LoginPage.TXT_LOGIN_INPUT).send_keys(login)
        self.find_element(*locators.LoginPage.TXT_PASSWORD_INPUT).send_keys(password)
        return self

    def submit_form(self):
        """
        submit
        """
        from tests.yspryn.test_HW6.pages.catalog_page import CatalogPage

        self.click(*locators.LoginPage.BTN_SUBMIT)
        return CatalogPage(self.driver)
