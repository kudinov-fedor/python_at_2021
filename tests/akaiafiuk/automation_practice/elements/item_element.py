from selenium.webdriver.common.by import By
from tests.akaiafiuk.automation_practice.elements.base_element import BaseElement
from tests.akaiafiuk.automation_practice.pages.item_info_frame import ItemInfoFrame
from tests.akaiafiuk.automation_practice.pages.item_page import ItemPage


class ItemElement(BaseElement):
    IMAGE = By.CSS_SELECTOR, '.product-image-container'
    NAME = By.CSS_SELECTOR, '.product-name'
    MORE_BTN = By.CSS_SELECTOR, '.lnk_view'
    QUICK_VIEW = By.CSS_SELECTOR, '.quick-view'
    PRICE = By.CSS_SELECTOR, '.right-block'

    def open_item(self) -> ItemPage:
        self.find_element(ItemElement.NAME).click()
        return ItemPage(self.session.parent)

    @property
    def text(self):
        return self.find_element(ItemElement.NAME).text

    def click_more_button(self):
        self.hover()
        self.find_element(ItemElement.MORE_BTN).click()
        return ItemPage(self.session.parent)

    def open_item_info(self) -> ItemInfoFrame:
        self.hover()
        self.find_element(ItemElement.QUICK_VIEW).click()
        return ItemInfoFrame(self.parent())
