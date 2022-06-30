from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from tests.akaiafiuk.automation_practice.pages.base_frame import BaseFrame


class ItemInfoFrame(BaseFrame):
    NAME = By.CSS_SELECTOR, 'h1'
    DESCRIPTION = By.CSS_SELECTOR, '#short_description_content p'
    PRICE = By.CSS_SELECTOR, '.our_price_display'
    MAIN_IMAGE = By.CSS_SELECTOR, '#bigpic'
    IMAGES = By.CSS_SELECTOR, '.img-responsive'
    CLOSE_ICON = By.CSS_SELECTOR, '.fancybox-close'

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.switch_to.default_content()
        self.close

    @property
    def name(self) -> str:
        return self.find_element(ItemInfoFrame.NAME).text

    @property
    def description(self) -> str:
        return self.find_element(ItemInfoFrame.DESCRIPTION).text

    @property
    def price(self) -> str:
        return self.find_element(ItemInfoFrame.PRICE).text

    @property
    def main_image(self) -> WebElement:
        return self.find_element(ItemInfoFrame.MAIN_IMAGE)

    @property
    def images(self) -> List[WebElement]:
        return self.find_elements(ItemInfoFrame.IMAGES)

    @property
    def close(self):
        self.session.find_element(*ItemInfoFrame.CLOSE_ICON).click()
