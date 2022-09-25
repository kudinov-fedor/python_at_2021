from selenium.webdriver.support.wait import WebDriverWait

from tests.dnazar.pom import text_box_page_locators as locators
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TextBoxPageElements:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_full_name_input(self):
        return WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, locators.FULL_NAME_INPUT)))

    def get_email_input(self):
        return WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, locators.EMAIL_INPUT)))

    def get_current_address_textarea(self):
        return WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, locators.CURRENT_ADDRESS_TEXTAREA)))

    def get_permanent_address_textarea(self):
        return WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, locators.PERMANENT_ADDRESS_TEXTAREA)))

    def get_submit_button(self):
        return WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, locators.SUBMIT_BUTTON)))

    def get_name_text(self):
        return WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, locators.NAME_TEXT)))

    def get_email_text(self):
        return WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, locators.EMAIL_TEXT)))

    def get_current_address_text(self):
        return WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, locators.CURRENT_ADDRESS_TEXT)))

    def get_permanent_address_text(self):
        return WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, locators.PERMANENT_ADDRESS_TEXT)))
