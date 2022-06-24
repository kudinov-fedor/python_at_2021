from selenium.webdriver.common.by import By
from python_at_2021.tests.akaiafiuk.automation_practice.pages import MainPage


class SearchPage(MainPage):

    SEARCH_TEXT = By.CSS_SELECTOR, '.lighter'

    @property
    def search_text(self) -> str:
        return self.find_element(SearchPage.SEARCH_TEXT).text
