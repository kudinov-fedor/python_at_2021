from selenium.webdriver.remote.webdriver import WebDriver
from tests.dnazar.pom.text_box_page_elements import TextBoxPageElements
from tests.dnazar.context.base_context import BaseContext


class TextBoxPageContext(BaseContext):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.elements = TextBoxPageElements(self.driver)

    def fill_full_name_field(self, value: str):
        self.fill_field(self.elements.get_full_name_input(), value)
        return self

    def fill_email_field(self, value: str):
        self.fill_field(self.elements.get_email_input(), value)
        return self

    def fill_current_address_field(self, value: str):
        self.fill_field(self.elements.get_current_address_textarea(), value)
        return self

    def fill_permanent_address_field(self, value: str):
        self.fill_field(self.elements.get_permanent_address_textarea(), value)
        return self

    def click_submit_button(self):
        self.click_button(self.elements.get_submit_button())
        return self

    def verify_name_output_text_contains(self, expected: str):
        self.verify_element_contains_text(self.elements.get_name_text(), expected)
        return self

    def verify_email_output_text_contains(self, expected: str):
        self.verify_element_contains_text(self.elements.get_email_text(), expected)
        return self

    def verify_cur_adr_output_text_contains(self, expected: str):
        self.verify_element_contains_text(self.elements.get_current_address_text(), expected)
        return self

    def verify_per_adr_output_text_contains(self, expected: str):
        self.verify_element_contains_text(self.elements.get_permanent_address_text(), expected)
        return self
