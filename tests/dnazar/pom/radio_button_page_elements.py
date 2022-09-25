from selenium.webdriver.support.wait import WebDriverWait
from tests.dnazar.pom import radio_button_page_locators as locators
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class RadioButtonPageElements:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_yes_input(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, locators.YES_INPUT)))

    def get_impressive_input(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, locators.IMPRESSIVE_INPUT)))

    def get_no_input(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, locators.NO_INPUT)))
