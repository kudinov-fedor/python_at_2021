from typing import Tuple

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement


class BaseElement:
    def __init__(self, locator: WebElement):
        self.locator = locator

    def element(self, by: Tuple[By, str]):
        return self.locator.find_element(*by)

    def collection(self, by: Tuple[By, str]):
        return self.locator.find_elements(*by)

    def click(self):
        element = self
        action =  ActionChains(self.locator)
        action.move_to_element(element).click().perform()
        return self

