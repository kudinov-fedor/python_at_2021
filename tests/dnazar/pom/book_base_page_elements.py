from tests.dnazar.pom import book_base_page_locators as locators
from tests.dnazar.pom.common_book_store_elements import CommonBookStoreElements


class BookBasePageElements(CommonBookStoreElements):

    def get_search_input(self):
        return self.get_element(locators.SEARCH_INPUT)

    def get_book_items(self):
        return self.get_elements(locators.BOOK_ITEMS, 2)

    def get_book_item_link(self, book_name: str):
        return self.get_element(locators.book_item_link(book_name), 2)

    def get_add_to_collection_button(self):
        return self.get_element(locators.ADD_TO_COLLECTION_BUTTON, 5)

    def get_back_to_store_button(self):
        return self.get_element(locators.BACK_TO_STORE_BUTTON, 3)
