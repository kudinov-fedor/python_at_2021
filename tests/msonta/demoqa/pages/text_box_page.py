from selenium.webdriver.remote.webdriver import WebDriver
from tests.msonta.demoqa.pages.base_page import BasePage


class TextBoxPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def submit(self, locator):
        self.driver.execute_script("window.scrollTo(0, 500);")
        self.driver.find_element(*locator).click()

    def fill_full_name(self, locator, full_name):
        full_name_field = self.driver.find_element(*locator)
        full_name_field.clear()
        full_name_field.send_keys(full_name)

    def get_full_name_text(self, locator):
        return self.driver.find_element(*locator).text

    def fill_email(self, locator, email):
        email_field = self.driver.find_element(*locator)
        email_field.clear()
        email_field.send_keys(email)

    def get_email_text(self, locator):
        return self.driver.find_element(*locator).text

    def fill_current_address(self, locator, current_address):
        current_address_field = self.driver.find_element(*locator)
        current_address_field.clear()
        current_address_field.send_keys(current_address)

    def get_current_address_text(self, locator):
        return self.driver.find_element(*locator).text

    def fill_permanent_address(self, locator, permanent_address):
        permanent_address_field = self.driver.find_element(*locator)
        permanent_address_field.clear()
        permanent_address_field.send_keys(permanent_address)

    def get_permanent_address_text(self, locator):
        return self.driver.find_element(*locator).text
