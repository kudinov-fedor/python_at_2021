import pytest
from tests.ylond import pageObject as pages
from faker import Faker
from random import randrange


@pytest.mark.usefixtures("session")
def test_employee_registration(session):
    web_pages = pages.WebPages(session).open()
    web_pages.get_fill_form().employee_registration("Yuliia", "Londarenko", "abc@gmail.com", "1000", "45", "test")

    assert web_pages.get_web_table().get_employee_register_result() == True


def test_employee_edit(session):
    web_pages = pages.WebPages(session).open()
    assert web_pages.get_web_table().is_edit_button_present(), "no edit button"

    web_pages.get_web_table().click_edit_button()
    web_pages.get_pop_up().edit_employee("123")

    assert web_pages.get_web_table().get_first_name_result() == "123"


def test_employee_remove(session):
    web_pages = pages.WebPages(session).open()
    web_pages.get_web_table().remove_employee()

    assert web_pages.get_web_table().is_remove_button_present() == False


def test_employee_search(session):
    web_pages = pages.WebPages(session).open()
    web_pages.get_fill_form().employee_registration("Yuliia", "Londarenko", "abc@gmail.com", "1000", "45", "test")
    web_pages.get_web_table().search_employee_by_first_name("Yuliia")

    assert web_pages.get_web_table().get_first_name_result() == "Yuliia"


def test_get_total_pages(session):
    web_pages = pages.WebPages(session).open()
    fake = Faker()
    for i in range(15):
        web_pages.get_fill_form().employee_registration(fake.first_name(), fake.last_name(), fake.email(), str(randrange(18, 60)), str(randrange(100, 5000000)), fake.company())
    web_pages.scroll_down()

    assert web_pages.get_web_table().get_total_pages() == "2"
