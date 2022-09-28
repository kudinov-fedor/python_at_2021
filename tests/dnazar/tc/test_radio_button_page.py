from tests.dnazar import context
from tests.dnazar import constants


def test_radio_buttons_are_enabled(session):
    my_context = context.RadioButtonPageContext(session)

    my_context.open_page(constants.RADIO_BUTTON_PAGE_LINK) \
        .verify_yes_radio_button_is_enabled(True) \
        .verify_no_radio_button_is_enabled(False) \
        .verify_impressive_radio_button_is_enabled(True)
