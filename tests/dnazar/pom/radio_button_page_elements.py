from tests.dnazar.pom import radio_button_page_locators as locators
from tests.dnazar.pom.base_element import BaseElement


class RadioButtonPageElements(BaseElement):

    def get_yes_input(self):
        return self.get_element(locators.YES_INPUT)

    def get_impressive_input(self):
        return self.get_element(locators.IMPRESSIVE_INPUT)

    def get_no_input(self):
        return self.get_element(locators.NO_INPUT)
