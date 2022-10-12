from tests.dnazar.pom import book_base_page_locators as locators
from tests.dnazar.pom.common_book_store_elements import CommonBookStoreElements


class AddBookPageElements(CommonBookStoreElements):

    def get_add_to_collection_button(self):
        return self.get_element(locators.ADD_TO_COLLECTION_BUTTON, 6)

    def get_back_to_store_button(self):
        return self.get_element(locators.BACK_TO_STORE_BUTTON, 3)
