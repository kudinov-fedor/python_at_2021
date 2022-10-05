from selenium.webdriver.remote.webdriver import WebDriver
from tests.dnazar.context.base_context import BaseContext
from tests.dnazar.pom.common_book_store_elements import CommonBookStoreElements


class CommonBookStoreContext(BaseContext):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.elements = CommonBookStoreElements(self.driver)

    def click_logout_button(self):
        return self.click_button(self.elements.get_logout_button())

    def verify_logout_button_enabled(self, expected=True):
        return self.verify_element_is_enabled(self.elements.get_logout_button(), expected)
