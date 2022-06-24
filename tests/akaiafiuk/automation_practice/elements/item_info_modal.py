from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from python_at_2021.tests.akaiafiuk.automation_practice.elements.base_element import BaseElement


class ItemInfoModal(BaseElement):
    NAME = By.CSS_SELECTOR, 'h1'
    DESCRIPTION = By.CSS_SELECTOR, '#short_description_content p'
    PRICE = By.CSS_SELECTOR, '.our_price_display'
    MAIN_IMAGE = By.CSS_SELECTOR, '#bigpic'
    IMAGES = By.CSS_SELECTOR, '.img-responsive'

    @property
    def name(self) -> str:
        return self.find_element(ItemInfoModal.NAME).text

    @property
    def description(self) -> str:
        return self.find_element(ItemInfoModal.DESCRIPTION).text

    @property
    def price(self) -> str:
        return self.find_element(ItemInfoModal.PRICE).text

    @property
    def main_image(self) -> WebElement:
        return self.find_element(ItemInfoModal.MAIN_IMAGE)

    @property
    def images(self) -> List[WebElement]:
        return self.find_elements(ItemInfoModal.IMAGES)
