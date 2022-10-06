from tests.msonta.demoqa.pages.text_box_page import TextBoxPage
from tests.msonta.demoqa import config


def test_full_name(session):
    text_box_page = TextBoxPage(session)
    text_box_page.open()
    text_box_page.fill_field(locator=text_box_page.locators.full_name_input, text=config.NAME)
    text_box_page.scroll_down_page()
    text_box_page.left_click(text_box_page.locators.submit_button)

    assert f"Name:{config.NAME}" == text_box_page.get_text(text_box_page.locators.full_name_text)


def test_email(session):
    text_box_page = TextBoxPage(session)
    text_box_page.open()
    text_box_page.fill_field(locator=text_box_page.locators.email_input, text=config.EMAIL)
    text_box_page.scroll_down_page()
    text_box_page.left_click(text_box_page.locators.submit_button)

    assert f"Email:{config.EMAIL}" == text_box_page.get_text(text_box_page.locators.email_text)


def test_current_address(session):
    text_box_page = TextBoxPage(session)
    text_box_page.open()
    text_box_page.fill_field(locator=text_box_page.locators.current_address_input, text=config.CURRENT_ADDRESS)
    text_box_page.scroll_down_page()
    text_box_page.left_click(text_box_page.locators.submit_button)

    assert f"Current Address :{config.CURRENT_ADDRESS}" == text_box_page.get_text(
        text_box_page.locators.current_address_text)


def test_provide_permanent_address(session):
    text_box_page = TextBoxPage(session)
    text_box_page.open()
    text_box_page.fill_field(locator=text_box_page.locators.permanent_address_input, text=config.PERMANENT_ADDRESS)
    text_box_page.scroll_down_page()
    text_box_page.left_click(text_box_page.locators.submit_button)

    assert f"Permananet Address :{config.PERMANENT_ADDRESS}" == text_box_page.get_text(
        text_box_page.locators.permanent_address_text)
