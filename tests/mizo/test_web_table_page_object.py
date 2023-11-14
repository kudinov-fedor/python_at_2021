from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.mizo.constants import HOST2
from tests.mizo.web_table_page_object import WebPage, Registration


def test_new_record_added(driver):
    driver.get(HOST2 + "/webtables")
    web_page = WebPage(driver)

    registration_modal = web_page.create_element()
    registration_modal.fill_form(first_name="Mariia", last_name="selenium", email="selenium@gmail.com", age=20,
                                 salary=3000, department='local')
    registration_modal.click_submit_button()
    rows = web_page.get_rows()
    rows_count = len(rows)

    last_row = rows[-1]
    cells = last_row.get_cells()
    assert cells.first_name == "Mariia"
    assert rows_count == 4


def test_edited_new_record(driver):
    driver.get(HOST2 + "/webtables")
    web_page = WebPage(driver)
    rows = web_page.get_rows()
    rows[1].click_edit()
    registration_modal = Registration(driver)
    registration_modal.fill_form(salary=4000)
    registration_modal.click_submit_button()
    edited_row = rows[1]
    cells = edited_row.get_cells()
    assert cells.salary == "4000"


def test_deleted_record(driver):
    driver.get(HOST2 + "/webtables")
    web_page = WebPage(driver)
    rows_before_delete = web_page.get_rows()
    assert len(rows_before_delete) == 3
    rows_before_delete[0].click_delete()
    rows_after_delete = len(web_page.get_rows())
    assert rows_after_delete == 2


def test_search_box(driver):
    driver.get(HOST2 + "/webtables")
    web_page = WebPage(driver)
    web_page.fill_search_field("Cierra")
    rows_after_search = web_page.get_rows()
    assert len(rows_after_search) == 1
