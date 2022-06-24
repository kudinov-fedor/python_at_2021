from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from python_at_2021.tests.akaiafiuk.automation_practice.pages.base_page import BasePage


class ItemPage(BasePage):
    ITEM_NAME = By.XPATH, './/*[@itemprop="name"]'
    ITEM_DESCRIPTION = By.CSS_SELECTOR, '#short_description_content p'
    ITEM_IMAGE = By.CSS_SELECTOR, '#bigpic'
    PRICE = By.CSS_SELECTOR, '#our_price_display'

    @property
    def name(self) -> str:
        return self.find_element(ItemPage.ITEM_NAME).text

    @property
    def description(self) -> str:
        return self.find_element(ItemPage.ITEM_DESCRIPTION).text

    @property
    def image(self) -> WebElement:
        return self.find_element(ItemPage.ITEM_IMAGE)

    @property
    def price(self) -> str:
        return self.find_element(ItemPage.PRICE).text
