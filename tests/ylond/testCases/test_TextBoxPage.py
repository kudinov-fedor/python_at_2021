import pytest
from tests.ylond.pageObject import TextBoxPage


@pytest.mark.usefixtures("session")
def test_elements_presence(session):
    tb = TextBoxPage.TextBoxPage(session).open()
    assert tb.presence_full_name() == "Full Name"
    assert tb.presence_email() == "Email"
    assert tb.presence_current_address() == "Current Address"
    assert tb.presence_permanent_address() == "Permanent Address"


def test_full_name_input_field(session):
    tb = TextBoxPage.TextBoxPage(session).open()
    tb.enter_full_name("test")
    tb.scroll_down()
    tb.click_submit_button()
    assert tb.get_username_text() == "Name:test"


def test_absence_result_all_empty_fields(session):
    tb = TextBoxPage.TextBoxPage(session).open()
    tb.scroll_down()
    tb.click_submit_button()
    assert tb.is_element_present() == False


def test_email_error_input_field(session):
    tb = TextBoxPage.TextBoxPage(session).open()
    tb.enter_email("test1")
    tb.scroll_down()
    tb.click_submit_button()
    tb.scroll_up()
    assert tb.get_error_email_result() == True


def test_all_submit_form(session):
    tb = TextBoxPage.TextBoxPage(session).open()
    tb.enter_full_name("Yuliia Londarenko")
    tb.enter_email("test@gmail.com")
    tb.enter_current_address("CurrentAddress")
    tb.enter_permanent_address("Permanent Address")
    tb.scroll_down()
    tb.click_submit_button()
    assert tb.get_submit_result() == 'Name:Yuliia Londarenko\n' 'Email:test@gmail.com\n' 'Current Address :CurrentAddress\n' 'Permanent Address :Permanent Address'

#example with fill_form method
def test_all_submit_form_1(session):
    tb = TextBoxPage.TextBoxPage(session).open()
    tb.fill_form("Yuliia Londarenko", "test@gmail.com", "CurrentAddress", "Permanent Address")
    assert tb.get_submit_result() == 'Name:Yuliia Londarenko\n' 'Email:test@gmail.com\n' 'Current Address :CurrentAddress\n' 'Permanent Address :Permanent Address'
