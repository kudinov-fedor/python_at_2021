from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
from python_at_2021.tests.akaiafiuk.automation_practice.elements.base_element import BaseElement
from python_at_2021.tests.akaiafiuk.automation_practice.elements.item_info_modal import ItemInfoModal
from python_at_2021.tests.akaiafiuk.automation_practice.pages.item_page import ItemPage


class ItemElement(BaseElement):
    IMAGE = By.CSS_SELECTOR, '.product-image-container'
    NAME = By.CSS_SELECTOR, '.product-name'
    MORE_BTN = By.CSS_SELECTOR, '.lnk_view'
    ITEM_INFO_MODAL = By.XPATH, './/*[@id="product"]'

    def open_item(self) -> ItemPage:
        self.find_element(ItemElement.NAME).click()
        return ItemPage(self.session.parent)

    @property
    def text(self):
        return self.find_element(ItemElement.NAME).text

    def move_highlight(self):
        action = AC(self.parent())
        action.move_to_element(self.session)
        action.perform()

    def click_more_button(self):
        self.move_highlight()
        self.find_element(ItemElement.MORE_BTN).click()
        return ItemPage(self.session.parent)

    def open_item_info(self) -> ItemInfoModal:
        self.move_highlight()
        self.find_element(ItemElement.IMAGE).click()
        # todo: fails here because couldn't find element inside element
        return ItemInfoModal(self.find_element(ItemElement.ITEM_INFO_MODAL))
