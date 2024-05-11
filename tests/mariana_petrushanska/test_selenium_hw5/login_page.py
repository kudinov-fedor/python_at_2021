from tests.mariana_petrushanska.test_selenium_hw5.base_page import BasePage
from tests.mariana_petrushanska.test_selenium_hw5.product_page import ProductsPage
from tests.mariana_petrushanska.test_selenium_hw5.locators import LoginPageLoc


class LoginPage(BasePage):

    def fill_in_login_form(self, login: str, password: str):
        """
        Fill in login form
        """
        self.find_element(*LoginPageLoc.TXT_USERNAME).send_keys(login)
        self.find_element(*LoginPageLoc.TXT_PASSWORD).send_keys(password)
        return self

    def confirm_login(self) -> ProductsPage:
        """
        Confirm login (submit login form)
        """
        self.find_element(*LoginPageLoc.BTN_LOGIN).click()
        return ProductsPage(self.driver)
