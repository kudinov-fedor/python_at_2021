from tests.dnazar.pom import common_book_store_locators as locators
from tests.dnazar.pom.base_element import BaseElement


class CommonBookStoreElements(BaseElement):

    def get_logout_button(self):
        return self.get_element(locators.LOGOUT_BUTTON, 2)
