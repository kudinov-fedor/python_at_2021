from typing import List

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from tests.osokolov.book_store.base_element import BaseElement
from tests.osokolov.book_store.base_page import BasePage
from tests.osokolov.book_store.book_store_elements import BookStoreElements
from tests.osokolov.book_store.login_page import LoginPage


class BookStorePage(BasePage):
    HOST = 'https://demoqa.com'
    URL = '/books'

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.book_store_elements = BookStoreElements()

    def input_search_field(self, text):
        search_box = self.element(self.book_store_elements.search_box)
        search_box.clear()
        search_box.send_keys(text)
        return self

    def click_login_button(self):
        self.element(self.book_store_elements.login_button).click()
        return LoginPage(self.driver)

    def get_books_count(self):
        len(self.collection(self.book_store_elements.table_row))
        return self

    def sort_by_image(self):
        self.element(self.book_store_elements.image).click()

    def sort_by_title(self):
        self.element(self.book_store_elements.title).click()

    def sort_by_author(self):
        self.element(self.book_store_elements.author).click()

    def sort_by_publisher(self):
        self.element(self.book_store_elements.publisher).click()

    def get_user_name(self):
        assert self.element(self.book_store_elements.user_name).text
        return self

    def verify_log_out_button(self):
        try:
            self.element(self.book_store_elements.log_out_button).is_displayed()
        except NoSuchElementException:
            return False

    def get_book_rows(self) -> List['BookRow']:
        rows = self.collection(self.book_store_elements.table_row)
        return [BookRow(row) for row in rows]


class BookRow(BaseElement):

    def get_title(self) -> str:
        return self.element((By.XPATH, './div/div[2]')).text

    def get_author(self) -> str:
        return self.element((By.XPATH, './div/div[3]')).text

    def get_publisher(self) -> str:
        return self.element((By.XPATH, './div/div[4]')).text
