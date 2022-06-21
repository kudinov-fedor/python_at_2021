from selenium.webdriver.common.by import By
from python_at_2021.tests.akaiafiuk.automation_practice.elements.base_element import BaseElement


class CategoryElement(BaseElement):
    LINK = By.XPATH, '//li'

    def open_category(self):
        from python_at_2021.tests.akaiafiuk.automation_practice.pages.category_page import CategoryPage
        self.find_element(CategoryElement.LINK).click()
        return CategoryPage(self.session.parent)

    @property
    def text(self):
        return self.find_element(self.LINK).text
