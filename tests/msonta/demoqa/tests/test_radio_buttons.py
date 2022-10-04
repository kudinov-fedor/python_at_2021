from tests.msonta.demoqa.pages.radio_button_page import RadioButtonsPage


def test_yes_radio_button(open_radio_button_page):
    radio_button_page = RadioButtonsPage(open_radio_button_page)
    state = radio_button_page.check_element_is_disabled(radio_button_page.locators.yes_radio)

    assert True == state


def test_impressive_radio_button(open_radio_button_page):
    radio_button_page = RadioButtonsPage(open_radio_button_page)
    state = radio_button_page.check_element_is_disabled(radio_button_page.locators.impressive_radio)

    assert True == state


def test_no_radio_button(open_radio_button_page):
    radio_button_page = RadioButtonsPage(open_radio_button_page)
    state = radio_button_page.check_element_is_disabled(radio_button_page.locators.no_radio)

    assert False == state
