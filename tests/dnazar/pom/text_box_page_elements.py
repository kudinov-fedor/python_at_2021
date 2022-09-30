from tests.dnazar.pom import text_box_page_locators as locators
from tests.dnazar.pom.base_element import BaseElement


class TextBoxPageElements(BaseElement):

    def get_full_name_input(self):
        return self.get_element(locators.FULL_NAME_INPUT)

    def get_email_input(self):
        return self.get_element(locators.EMAIL_INPUT)

    def get_current_address_textarea(self):
        return self.get_element(locators.CURRENT_ADDRESS_TEXTAREA)

    def get_permanent_address_textarea(self):
        return self.get_element(locators.PERMANENT_ADDRESS_TEXTAREA)

    def get_submit_button(self):
        return self.get_element(locators.SUBMIT_BUTTON)

    def get_name_text(self):
        return self.get_element(locators.NAME_TEXT)

    def get_email_text(self):
        return self.get_element(locators.EMAIL_TEXT)

    def get_current_address_text(self):
        return self.get_element(locators.CURRENT_ADDRESS_TEXT)

    def get_permanent_address_text(self):
        return self.get_element(locators.PERMANENT_ADDRESS_TEXT)
