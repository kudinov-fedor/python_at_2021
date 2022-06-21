from typing import List
from selenium.webdriver.common.by import By
from python_at_2021.tests.akaiafiuk.automation_practice.pages.base_page import BasePage
from python_at_2021.tests.akaiafiuk.automation_practice.elements.item_element import ItemElement


class MainPage(BasePage):
    ITEM = By.CSS_SELECTOR, '[class="product-container"]'

    @property
    def items(self) -> List[ItemElement]:
        return [ItemElement(element) for element in self.find_elements(MainPage.ITEM)]
