from selenium.webdriver.remote.webdriver import WebDriver
from tests.dnazar.context.base_context import BaseContext
from tests.dnazar.pom.modal_window_elements import ModalWindowElements


class ModalWindowContext(BaseContext):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.elements = ModalWindowElements(self.driver)

    def click_ok_button_modal_window(self):
        return self.click_button(self.elements.get_ok_button())
