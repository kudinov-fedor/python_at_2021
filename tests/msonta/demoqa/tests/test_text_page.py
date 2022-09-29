from tests.msonta.demoqa.pages.text_box_page import TextBoxPage
from tests.msonta.demoqa import config
from tests.msonta.demoqa.locators import TextBoxPageLocators as locators


def test_full_name(open_text_box_page):
    text_box_page = TextBoxPage(open_text_box_page)
    text_box_page.fill_full_name(locator=locators.full_name_input, full_name=config.NAME)
    text_box_page.submit(locators.submit_button)

    assert f"Name:{config.NAME}" == text_box_page.get_full_name_text(locators.full_name_text)


def test_email(open_text_box_page):
    text_box_page = TextBoxPage(open_text_box_page)
    text_box_page.fill_email(locator=locators.email_input, email=config.EMAIL)
    text_box_page.submit(locators.submit_button)

    assert f"Email:{config.EMAIL}" == text_box_page.get_email_text(locators.email_text)


def test_current_address(open_text_box_page):
    text_box_page = TextBoxPage(open_text_box_page)
    text_box_page.fill_current_address(locator=locators.current_address_input, current_address=config.CURRENT_ADDRESS)
    text_box_page.submit(locators.submit_button)

    assert f"Current Address :{config.CURRENT_ADDRESS}" == text_box_page.get_current_address_text(locators.current_address_text)


def test_provide_permanent_address(open_text_box_page):
    text_box_page = TextBoxPage(open_text_box_page)
    text_box_page.fill_permanent_address(locator=locators.permanent_address_input, permanent_address=config.PERMANENT_ADDRESS)
    text_box_page.submit(locators.submit_button)

    assert f"Permananet Address :{config.PERMANENT_ADDRESS}" == text_box_page.get_permanent_address_text(locators.permanent_address_text)
