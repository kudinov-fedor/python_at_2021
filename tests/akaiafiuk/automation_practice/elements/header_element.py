from typing import List
from selenium.webdriver.common.by import By
from python_at_2021.tests.akaiafiuk.automation_practice.elements.category_element import CategoryElement
from python_at_2021.tests.akaiafiuk.automation_practice.elements.base_element import BaseElement


class HeaderElement(BaseElement):
    CATEGORIES = By.XPATH, '//*[contains(@class, "sf-menu")]'

    @property
    def categories(self) -> List[CategoryElement]:
        return [CategoryElement(element) for element in self.find_elements(HeaderElement.CATEGORIES)]
