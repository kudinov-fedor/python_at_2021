from selenium.webdriver.remote.webdriver import WebDriver
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
        return self.click_button(self.elements.get_book_item_link(book_title))

    def click_add_to_collection_button(self):
        self.scroll_down()
        return self.click_button(self.elements.get_add_to_collection_button())

    def click_back_to_store_button(self):
        self.scroll_down()
        return self.click_button(self.elements.get_back_to_store_button())

    def verify_books_count(self, expected: int):
        assert expected == len(self.elements.get_book_items())
        return self
