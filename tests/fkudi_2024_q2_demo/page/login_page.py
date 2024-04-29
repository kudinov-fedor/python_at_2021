from selenium.webdriver.common.by import By

from tests.fkudi_some.page.base_page import BasePage
from tests.fkudi_some.page.catalog_page import CatalogPage


class LoginPage(BasePage):

    def open(self):
        self.driver.get("https://www.saucedemo.com")
        return self

    def fill_form(self, login: str, password: str) :
        """
        1. заповненя
        """
        self.find_element(By.ID, "user-name").send_keys(login)
        self.find_element(By.ID, "password").send_keys(password)
        return self

    def submit_form(self) -> CatalogPage:
        """
        2. сабміт
        """

        self.click(By.ID, "login-button", wait=2)

        return CatalogPage(self.driver)





