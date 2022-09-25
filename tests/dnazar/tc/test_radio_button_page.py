from tests.dnazar.context.radio_button_page_context import RadioButtonPageContext
from tests.dnazar import constants


class TestRadioButton:

    def test_radio_buttons_are_enabled(self, session):
        context = RadioButtonPageContext(session)

        context.open_page(constants.RADIO_BUTTON_PAGE_LINK) \
            .verify_yes_radio_button_is_enabled(True) \
            .verify_no_radio_button_is_enabled(False) \
            .verify_impressive_radio_button_is_enabled(True)
