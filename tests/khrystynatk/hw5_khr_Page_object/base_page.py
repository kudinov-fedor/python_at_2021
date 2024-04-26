from selenium.webdriver.remote.webdriver import WebDriver
from tests.khrystynatk.hw5_khr_Page_object.locators1 import LoginPageLoc


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self, host):
        self.driver.get(host)

    def get_url(self):
        return self.driver.current_url

    def find_username_field(self):
        return self.driver.find_element(*LoginPageLoc.TXT_USERNAME)

    def find_password_field(self):
        return self.driver.find_element(*LoginPageLoc.TXT_PASSWORD)
