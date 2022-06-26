from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tests.akaiafiuk.automation_practice.pages.base_page import BasePage
from tests.akaiafiuk.automation_practice.elements.item_element import ItemElement


class MainPage(BasePage):
    ITEM = By.CSS_SELECTOR, '[class="product-container"]'
    SEARCH = By.CSS_SELECTOR, '.search_query'
    COLUMNS = By.CSS_SELECTOR, '[class="columns-container"]'
    ITEM_INFO_MODAL = By.CSS_SELECTOR, '#product'

    @property
    def items(self) -> List[ItemElement]:
        return [ItemElement(element) for element in self.find_elements(MainPage.ITEM)]

    def do_search(self, text: str):
        from tests.akaiafiuk.automation_practice.pages.search_page import SearchPage
        search_input = self.find_element(MainPage.SEARCH)
        search_input.clear()
        search_input.send_keys(text)
        search_input.send_keys(Keys.ENTER)
        return SearchPage(self.session)
