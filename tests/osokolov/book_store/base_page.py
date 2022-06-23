from typing import Tuple, List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    HOST = None
    URL = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    def title(self):
        return self.driver.title

    def open(self):
        return self.driver.get(f'{self.HOST}{self.URL}')

    def element(self, by: Tuple[By, str]) -> WebElement:
        return self.driver.find_element(*by)

    def collection(self, by: Tuple[By, str]) -> List[WebElement]:
        return self.driver.find_elements(*by)

    def refresh_page(self):
        self.driver.refresh()
