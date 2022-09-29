from tests.msonta.demoqa.pages.buttons_page import ButtonsPage
from tests.msonta.demoqa import config
from tests.msonta.demoqa.locators import ButtonPageLocators as locators


def test_double_click(open_button_page):
    buttons_page = ButtonsPage(open_button_page)
    buttons_page.double_click(locators.double_click_button)

    assert config.DOUBLE_CLICK_MSG == buttons_page.get_double_click_msg(locators.double_click_msg)


def test_right_click(open_button_page):
    buttons_page = ButtonsPage(open_button_page)
    buttons_page.right_click(locators.right_click_button)

    assert config.RIGHT_CLICK_MSG == buttons_page.get_right_click_msg(locators.right_click_msg)


def test_regular_click(open_button_page):
    buttons_page = ButtonsPage(open_button_page)
    buttons_page.regular_click(locators.click_me_button)

    assert config.REGURAL_CLICK_MSG == buttons_page.get_regular_click_msg(locators.click_me_msg)

