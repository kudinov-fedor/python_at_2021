from typing import List
from python_at_2021.tests.akaiafiuk.automation_practice.pages.base_page import BasePage
from python_at_2021.tests.akaiafiuk.automation_practice.elements.item_element import ItemElement


class MainPage(BasePage):

    def get_items(self) -> List[ItemElement]:
        # todo: return a list of Item
        ...
