from selenium.webdriver.remote.webdriver import WebDriver
from tests.dnazar.context.base_context import BaseContext
from tests.dnazar.pom.radio_button_page_elements import RadioButtonPageElements


class RadioButtonPageContext(BaseContext):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.elements = RadioButtonPageElements(self.driver)

    def verify_yes_radio_button_is_enabled(self, expected: bool):
        self.verify_element_is_enabled(self.elements.get_yes_input(), expected)
        return self

    def verify_impressive_radio_button_is_enabled(self, expected: bool):
        self.verify_element_is_enabled(self.elements.get_impressive_input(), expected)
        return self

    def verify_no_radio_button_is_enabled(self, expected: bool):
        self.verify_element_is_enabled(self.elements.get_no_input(), expected)
        return self
