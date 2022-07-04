from typing import Tuple, List
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement
from tests.akaiafiuk.automation_practice.utils import scroll_to_element


class BaseElement(WebElement):
    def __init__(self, session: WebElement):
        self.session = session

    def parent(self) -> WebDriver:
        return self.session.parent

    def find_element(self, by: Tuple[By, str]) -> WebElement:
        return self.session.find_element(*by)

    def find_elements(self, by: Tuple[By, str]) -> List[WebElement]:
        return self.session.find_elements(*by)

    def hover(self):
        action = AC(self.parent())
        scroll_to_element(self.parent(), self.session)
        action.move_to_element(self.session)
        action.perform()
