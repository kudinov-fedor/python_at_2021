from typing import Self
from tests.ysemenov.hw6.pages.base_page import BasePage
from tests.ysemenov.hw6.locators import LocatorsLoginPage
from tests.ysemenov.hw6.pages.inventory_page import InventoryPage


class LoginPage(BasePage):

    def fill_form(self, login: str, password: str) -> Self:
        self.send_keys(*LocatorsLoginPage.TXT_LOGIN, login)
        self.send_keys(*LocatorsLoginPage.TXT_PASSWORD, password)
        return self

    def submit_form(self) -> Self:
        self.click_by_locator(*LocatorsLoginPage.BTN_SUBMIT)
        return self

    def log_in(self, login: str, password: str) -> InventoryPage:
        self.fill_form(login, password)
        self.submit_form()
        return InventoryPage(self.driver)
