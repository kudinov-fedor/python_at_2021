from typing import Tuple, List
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement
from tests.akaiafiuk.constants import AUTOMATION_PRACTICE_HOST
from tests.akaiafiuk.automation_practice.elements.header_element import HeaderElement


class BasePage:
    url = ''
    HEADER = By.CSS_SELECTOR, '#header'

    def __init__(self, session: WebDriver):
        self.host = AUTOMATION_PRACTICE_HOST
        self.session = session

    def open(self):
        self.session.get(self.host + self.url)
        return self

    def find_element(self, by: Tuple[By, str]) -> WebElement:
        return self.session.find_element(*by)

    def find_elements(self, by: Tuple[By, str]) -> List[WebElement]:
        return self.session.find_elements(*by)

    def refresh_page(self):
        self.session.refresh()

    def on_load(self):
        WebDriverWait(self.session, 30).until(EC.url_contains(self.url))
        return self

    @property
    def header(self):
        return HeaderElement(self.find_element(BasePage.HEADER))
