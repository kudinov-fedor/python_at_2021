from tests.msonta.demoqa.pages.buttons_page import ButtonsPage
from tests.msonta.demoqa import config


def test_double_click(session):
    buttons_page = ButtonsPage(session)
    buttons_page.double_click()

    assert config.DOUBLE_CLICK_MSG == buttons_page.double_click_msg.text


def test_right_click(session):
    buttons_page = ButtonsPage(session)
    buttons_page.right_click()

    assert config.RIGHT_CLICK_MSG == buttons_page.right_click_msg.text


def test_regular_click(session):
    buttons_page = ButtonsPage(session)
    buttons_page.regular_click()

    assert config.REGURAL_CLICK_MSG == buttons_page.click_me_msg.text

