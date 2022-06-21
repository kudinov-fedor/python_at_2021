from selenium.webdriver.common.by import By
from python_at_2021.tests.akaiafiuk.automation_practice.elements.base_element import BaseElement
from python_at_2021.tests.akaiafiuk.automation_practice.pages.item_page import ItemPage


class ItemElement(BaseElement):
    IMAGE = By.CSS_SELECTOR, '.product-image-container'
    NAME = By.CSS_SELECTOR, '.product-name'
    MORE_BTN = By.CSS_SELECTOR, '.lnk_view'

    def open_item(self) -> ItemPage:
        self.find_element(ItemElement.NAME).click()
        return ItemPage(self.session.parent)

    @property
    def text(self):
        return self.find_element(ItemElement.NAME).text
