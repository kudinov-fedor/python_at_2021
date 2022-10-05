from tests.dnazar.pom import profile_page_locators as locators
from tests.dnazar.pom.book_base_page_elements import BookBasePageElements
from tests.dnazar.pom.modal_window_elements import ModalWindowElements


class ProfilePageElements(BookBasePageElements, ModalWindowElements):

    def get_book_item_delete_icon(self, book_name: str):
        return self.get_element(locators.book_item_delete_icon(book_name))

    def get_delete_all_books_button(self):
        return self.get_element(locators.DELETE_ALL_BOOKS_BUTTON)
