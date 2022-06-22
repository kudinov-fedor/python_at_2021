import pytest
from tests.ylond import pageObject as pages
from faker import Faker
from random import randrange


@pytest.mark.usefixtures("session")
def test_employee_registration(session):
    wt = pages.WebTables(session).open()
    wt.employee_registration("Yuliia", "Londarenko", "abc@gmail.com", "1000", "45", "test")

    assert wt.get_employee_register_result() == True


def test_employee_edit(session):
    wt = pages.WebTables(session).open()
    wt.edit_employee("123")

    assert wt.get_first_name_result() == "123"


def test_employee_remove(session):
    wt = pages.WebTables(session).open()
    wt.remove_employee()

    assert wt.is_remove_button_present() == False


def test_employee_search(session):
    wt = pages.WebTables(session).open()
    wt.employee_registration("Yuliia", "Londarenko", "abc@gmail.com", "1000", "45", "test")
    wt.search_employee_by_first_name("Yuliia")

    assert wt.get_first_name_result() == "Yuliia"


def test_get_total_pages(session):
    wt = pages.WebTables(session).open()
    fake = Faker()
    for i in range(15):
        wt.employee_registration(fake.first_name(), fake.last_name(), fake.email(), str(randrange(18, 55)), str(randrange(0, 5000000)), fake.company())
    wt.scroll_down()

    assert wt.get_total_pages() == "2"
