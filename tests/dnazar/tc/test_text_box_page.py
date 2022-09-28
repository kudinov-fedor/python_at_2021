from tests.dnazar import context
from tests.dnazar import constants


name = "Marry Wood"
email = "marry.wood@gmail.com"
current_Adr = "20 West 34th Street, New York, NY, United States"
permanent_Adr = "20 East 10th Street, New York, NY, United States"


def test_text_box_positive(session):
    my_context = context.TextBoxPageContext(session)

    my_context.open_page(constants.TEXT_BOX_PAGE_LINK) \
        .fill_full_name_field(name) \
        .fill_email_field(email) \
        .fill_current_address_field(current_Adr) \
        .fill_permanent_address_field(permanent_Adr) \
        .click_submit_button() \
        .verify_name_output_text_contains(name) \
        .verify_email_output_text_contains(email) \
        .verify_cur_adr_output_text_contains(current_Adr) \
        .verify_per_adr_output_text_contains(permanent_Adr)
