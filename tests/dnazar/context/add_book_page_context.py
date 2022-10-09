from selenium.webdriver.remote.webdriver import WebDriver
from tests.dnazar import context
from tests.dnazar.context.common_book_store_context import CommonBookStoreContext
from tests.dnazar.pom.add_book_page_elements import AddBookPageElements


class AddBookPageContext(CommonBookStoreContext):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.elements = AddBookPageElements(self.driver)

    def click_add_to_collection_button(self):
        self.scroll_down()
        return self.click_button(self.elements.get_add_to_collection_button())

    def click_back_to_store_button(self):
        self.scroll_down()
        self.click_button(self.elements.get_back_to_store_button())
        return context.BookBasePageContext(self.driver)
