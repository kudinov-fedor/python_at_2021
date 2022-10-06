from tests.msonta.demoqa.pages.radio_button_page import RadioButtonsPage


def test_yes_radio_button(session):
    radio_button_page = RadioButtonsPage(session)
    radio_button_page.open()
    state = radio_button_page.check_element_is_disabled(radio_button_page.locators.yes_radio)

    assert state


def test_impressive_radio_button(session):
    radio_button_page = RadioButtonsPage(session)
    radio_button_page.open()
    state = radio_button_page.check_element_is_disabled(radio_button_page.locators.impressive_radio)

    assert state


def test_no_radio_button(session):
    radio_button_page = RadioButtonsPage(session)
    radio_button_page.open()
    state = radio_button_page.check_element_is_disabled(radio_button_page.locators.no_radio)

    assert not state
