from typing import Tuple

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement


class BaseElement:
    def __init__(self, elem: WebElement):
        self.elem = elem


    def element(self, by: Tuple[By, str]):
        self.elem.find_element(*by)
        return self

    def collection(self, by: Tuple[By, str]):
        return self.elem.find_elements(*by)

    def click(self):
        self.elem.click()


