from tests.msonta.demoqa.locators import TextBoxPageLocators as locators
from selenium.webdriver.remote.webdriver import WebDriver
from tests.msonta.demoqa import config


class BasePage(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.full_name_text = ""
        self.email_text = ""
        self.current_address_text = ""
        self.permanent_address_text = ""


class TextBoxPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver.get(config.HOST + "text-box")

    def submit(self):
        self.driver.execute_script("window.scrollTo(0, 500);")
        self.driver.find_element(*locators.submit_button).click()

    def full_name(self, full_name):
        full_name_field = self.driver.find_element(*locators.full_name_input)
        full_name_field.clear()
        full_name_field.send_keys(full_name)

        self.submit()
        self.full_name_text = self.driver.find_element(*locators.full_name_text).text

    def email(self, email):
        email_field = self.driver.find_element(*locators.email_input)
        email_field.clear()
        email_field.send_keys(email)

        self.submit()
        self.email_text = self.driver.find_element(*locators.email_text).text

    def current_address(self, current_address):
        current_address_field = self.driver.find_element(*locators.current_address_input)
        current_address_field.clear()
        current_address_field.send_keys(current_address)

        self.submit()
        self.current_address_text = self.driver.find_element(*locators.current_address_text).text

    def permanent_address(self, permanent_address):
        permanent_address_field = self.driver.find_element(*locators.permanent_address_input)
        permanent_address_field.clear()
        permanent_address_field.send_keys(permanent_address)

        self.submit()
        self.permanent_address_text = self.driver.find_element(*locators.permanent_address_text).text
