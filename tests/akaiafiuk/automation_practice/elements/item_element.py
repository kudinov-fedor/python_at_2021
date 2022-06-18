from python_at_2021.tests.akaiafiuk.automation_practice.elements.base_element import BaseElement
from python_at_2021.tests.akaiafiuk.automation_practice.pages.item_page import ItemPage


class ItemElement(BaseElement):

    def open_item(self) -> ItemPage:
        ...
