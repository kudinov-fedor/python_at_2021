from tests.msonta.demoqa.pages.buttons_page import ButtonsPage
from tests.msonta.demoqa import config
import pytest


def test_double_click(session):
    buttons_page = ButtonsPage(session)
    buttons_page.open()
    buttons_page.double_click(buttons_page.locators.double_click_button)

    assert config.DOUBLE_CLICK_MSG == buttons_page.get_text(buttons_page.locators.double_click_msg)


@pytest.mark.xfail
def test_right_click(session):
    buttons_page = ButtonsPage(session)
    buttons_page.open()
    buttons_page.right_click(buttons_page.locators.right_click_button)

    assert config.RIGHT_CLICK_MSG == buttons_page.get_text(buttons_page.locators.right_click_msg)


def test_regular_click(session):
    buttons_page = ButtonsPage(session)
    buttons_page.open()
    buttons_page.left_click(buttons_page.locators.click_me_button)

    assert config.REGULAR_CLICK_MSG == buttons_page.get_text(buttons_page.locators.click_me_msg)
