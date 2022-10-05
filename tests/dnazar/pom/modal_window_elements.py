from tests.dnazar.pom import modal_window_locators as locators
from tests.dnazar.pom.base_element import BaseElement


class ModalWindowElements(BaseElement):

    def get_ok_button(self):
        return self.get_element(locators.OK_BUTTON)
