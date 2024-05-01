from tests.khrystynatk.pages.locators1 import LoginPageLoc
from tests.khrystynatk.pages.base_page import BasePage


class LoginPage(BasePage):

    def find_username_field(self):
        return self.driver.find_element(*LoginPageLoc.TXT_USERNAME)

    def find_password_field(self):
        return self.driver.find_element(*LoginPageLoc.TXT_PASSWORD)

    def input_creds(self, username, password):
        self.find_username_field().send_keys(username)
        self.find_password_field().send_keys(password)
        return self

    def submit_form(self):
        from tests.khrystynatk.pages.items_page import ItemsPage

        self.driver.find_element(*LoginPageLoc.BTN_LOGIN).click()
        return ItemsPage(self.driver)
