from typing import List
from selenium.webdriver.common.by import By
from python_at_2021.tests.akaiafiuk.automation_practice.pages.base_page import BasePage
from python_at_2021.tests.akaiafiuk.automation_practice.elements.item_element import ItemElement
from python_at_2021.tests.akaiafiuk.automation_practice.elements.header_element import HeaderElement


class MainPage(BasePage):
    ITEM = By.CSS_SELECTOR, '[class="product-container"]'
    HEADER = By.XPATH, '//*[@id="header_logo"]/parent::*'

    @property
    def items(self) -> List[ItemElement]:
        return [ItemElement(element) for element in self.find_elements(MainPage.ITEM)]

    @property
    def header(self):
        return HeaderElement(self.find_element(MainPage.HEADER))
