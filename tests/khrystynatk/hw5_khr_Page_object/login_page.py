from tests.khrystynatk.hw5_khr_Page_object.base_page import BasePage
from tests.khrystynatk.hw5_khr_Page_object.locators1 import LoginPageLoc


class LoginPage(BasePage):

    def open_login_page(self, host):
        self.open_page(host)

    def input_creds(self, username, password):
        self.driver.find_element(*LoginPageLoc.TXT_USERNAME).send_keys(username)
        self.driver.find_element(*LoginPageLoc.TXT_PASSWORD).send_keys(password)
        self.driver.find_element(*LoginPageLoc.BTN_LOGIN).click()
