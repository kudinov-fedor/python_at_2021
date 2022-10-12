from selenium.webdriver.remote.webdriver import WebDriver
from tests.dnazar.context.modal_window_context import ModalWindowContext
from tests.dnazar.context.book_base_page_context import BookBasePageContext
from tests.dnazar.pom.profile_page_elements import ProfilePageElements


class ProfilePageContext(BookBasePageContext, ModalWindowContext):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.elements = ProfilePageElements(self.driver)

    def on_load(self):
        return self.verify_logout_button_enabled()

    def click_book_delete_item(self, book_title: str):
        return self.click_button(self.elements.get_book_item_delete_icon(book_title))

    def click_delete_all_books_button(self):
        self.scroll_down()
        return self.click_button(self.elements.get_delete_all_books_button())
