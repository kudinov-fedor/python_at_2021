import pytest
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True, scope="function")
def test_setup(driver):
    driver.get("https://demoqa.com/webtables")


def test_add_entry(driver):
    add_btn = driver.find_element_by_id("addNewRecordButton")

    add_btn.click()

    first_name = driver.find_element_by_id("firstName")
    last_name = driver.find_element_by_id("lastName")
    email = driver.find_element_by_id("userEmail")
    age = driver.find_element_by_id("age")
    salary = driver.find_element_by_id("salary")
    department = driver.find_element_by_id("department")
    submit_btn = driver.find_element_by_id("submit")

    first_name.send_keys("Johnny")
    last_name.send_keys("Bravo")
    email.send_keys("jb@test.com")
    age.send_keys("19")
    salary.send_keys("15000")
    department.send_keys("HR")
    submit_btn.click()

    new_row = driver.find_elements_by_xpath("//div[@class='rt-tr-group']/div[div[text()='Johnny']]/div[not(div/span)]")
    expected_results = ["Johnny", "Bravo", "19", "jb@test.com", "15000", "HR"]

    for cell, expected in zip(new_row, expected_results):
        assert cell.text == expected


def test_edit_entry(driver):
    entry_edit_btn = driver.find_element_by_xpath("//div[div[text()='Alden']]//span[@id='edit-record-2']")

    entry_edit_btn.click()

    first_name = driver.find_element_by_id("firstName")
    submit_btn = driver.find_element_by_id("submit")

    first_name.clear()
    first_name.send_keys("Johnny")
    submit_btn.click()

    modified_row = driver.find_elements_by_xpath("//div[@class='rt-tr-group']/div[div[text()='Johnny']]/div[not("
                                                 "div/span)]")
    expected_results = ["Johnny", "Cantrell", "45", "alden@example.com", "12000", "Compliance"]

    for cell, expected in zip(modified_row, expected_results):
        assert cell.text == expected


def test_remove_entry(driver):
    entry_remove_btn = driver.find_element_by_xpath("//div[div[text()='Alden']]//span[@id='delete-record-2']")

    entry_remove_btn.click()

    removed_row = driver.find_elements_by_xpath("//div[@class='rt-tr-group']/div[div[text()='Alden']]")

    assert len(removed_row) == 0


@pytest.mark.parametrize("searched_name, expected_entry",
                         [("Cierra", ["Cierra", "Vega", "39", "cierra@example.com", "10000", "Insurance"]),
                          ("Alden", ["Alden", "Cantrell", "45", "alden@example.com", "12000", "Compliance"]),
                          ("Kierra", ["Kierra", "Gentry", "29", "kierra@example.com", "2000", "Legal"])])
def test_search_entry(searched_name, expected_entry, driver):
    search_box = driver.find_element_by_css_selector("#searchBox")

    search_box.send_keys(searched_name)

    # Search should return a single row with 6 data cells
    all_not_empty_rows_locator = "//div[@class='rt-tr-group']/div/div[not(span) and not(div/span)]"
    all_not_empty_rows = driver.find_elements(By.XPATH, all_not_empty_rows_locator)

    assert not len(all_not_empty_rows) > 6

    for cell, expected in zip(all_not_empty_rows, expected_entry):
        assert cell.text == expected
