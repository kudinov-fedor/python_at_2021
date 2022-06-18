from python_at_2021.tests.akaiafiuk.automation_practice.elements.base_element import BaseElement
from python_at_2021.tests.akaiafiuk.automation_practice.pages.category_page import CategoryPage


class ItemElement(BaseElement):

    def open_category(self) -> CategoryPage:
        ...
