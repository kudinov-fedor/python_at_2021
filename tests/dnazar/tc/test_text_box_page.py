from tests.dnazar.context.text_box_page_context import TextBoxPageContext
from tests.dnazar import constants


class TestTextBox:
    name = "Marry Wood"
    email = "marry.wood@gmail.com"
    current_Adr = "20 West 34th Street, New York, NY, United States"
    permanent_Adr = "20 East 10th Street, New York, NY, United States"

    def test_text_box_positive(self, session):
        context = TextBoxPageContext(session)

        context.open_page(constants.TEXT_BOX_PAGE_LINK) \
            .fill_full_name_field(self.name) \
            .fill_email_field(self.email) \
            .fill_current_address_field(self.current_Adr) \
            .fill_permanent_address_field(self.permanent_Adr) \
            .click_submit_button() \
            .verify_name_output_text_contains(self.name) \
            .verify_email_output_text_contains(self.email) \
            .verify_cur_adr_output_text_contains(self.current_Adr) \
            .verify_per_adr_output_text_contains(self.permanent_Adr)
