from selenium.webdriver.remote.webdriver import WebDriver
from tests.khrystynatk.hw5_khr_Page_object.locators1 import LoginPageLoc


class BasePage:
    from tests.khrystynatk.hw5_khr_Page_object.constants import HOST, USERNAME, PASSWORD

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        self.driver.get(BasePage.HOST)

    def input_creds(self, username, password):
        self.driver.find_element(*LoginPageLoc.TXT_USERNAME).send_keys(username)
        self.driver.find_element(*LoginPageLoc.TXT_PASSWORD).send_keys(password)
        self.driver.find_element(*LoginPageLoc.BTN_LOGIN).click()
