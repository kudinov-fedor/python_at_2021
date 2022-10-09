from selenium.webdriver.remote.webdriver import WebDriver

from tests.dnazar.context.add_book_page_context import AddBookPageContext
from tests.dnazar.context.common_book_store_context import CommonBookStoreContext
from tests.dnazar.pom.book_base_page_elements import BookBasePageElements


class BookBasePageContext(CommonBookStoreContext):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.elements = BookBasePageElements(self.driver)

    def fill_search_field(self, value: str):
        return self.fill_field(self.elements.get_search_input(), value)

    def clear_search_field(self):
        return self.clear_field(self.elements.get_search_input())

    def click_book_title_link(self, book_title: str):
        self.click_button(self.elements.get_book_item_link(book_title))
        return AddBookPageContext(self.driver)

    def verify_books_count(self, expected: int):
        assert expected == len(self.elements.get_book_items())
        return self
