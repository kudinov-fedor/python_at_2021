from tests.msonta.demoqa.pages.base_page import BasePage
from tests.msonta.demoqa.locators import TextBoxPageLocators


class TextBoxPage(BasePage):
    url = "text-box"
    locators = TextBoxPageLocators
