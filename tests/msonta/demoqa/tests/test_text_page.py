from tests.msonta.demoqa.pages.text_box_page import TextBoxPage
from tests.msonta.demoqa import config


def test_provide_full_name(session):
    text_box_page = TextBoxPage(session)
    text_box_page.full_name(config.NAME)

    assert f"Name:{config.NAME}" == text_box_page.full_name_text


def test_provide_email(session):
    text_box_page = TextBoxPage(session)
    text_box_page.email(config.EMAIL)

    assert f"Email:{config.EMAIL}" == text_box_page.email_text


def test_provide_current_address(session):
    text_box_page = TextBoxPage(session)
    text_box_page.current_address(config.CURRENT_ADDRESS)

    assert f"Current Address :{config.CURRENT_ADDRESS}" == text_box_page.current_address_text


def test_provide_permanent_address(session):
    text_box_page = TextBoxPage(session)
    text_box_page.permanent_address(config.PERMANENT_ADDRESS)

    assert f"Permananet Address :{config.PERMANENT_ADDRESS}" == text_box_page.permanent_address_text

