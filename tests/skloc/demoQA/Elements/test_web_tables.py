import pytest
from selenium.webdriver import Chrome


@pytest.fixture(autouse=True)
def test_setup():
    # driver = Chrome('C:\webdrivers\chromedriver.exe')
    global driver
    driver = Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/webtables")
    yield
    driver.close()
    driver.quit()


def test_add_entry():
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
    # "" for a last cell with edit and remove buttons
    expected_results = ["Johnny", "Bravo", "19", "jb@test.com", "15000", "HR"]
    iterator = 0

    for cell in new_row:
        assert cell.text == expected_results[iterator]
        iterator += 1


def test_edit_entry():
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
    iterator = 0

    for cell in modified_row:
        assert cell.text == expected_results[iterator]
        iterator += 1


def test_remove_entry():
    entry_remove_btn = driver.find_element_by_xpath("//div[div[text()='Alden']]//span[@id='delete-record-2']")

    entry_remove_btn.click()

    removed_row = driver.find_elements_by_xpath("//div[@class='rt-tr-group']/div[div[text()='Alden']]")

    assert len(removed_row) == 0


@pytest.mark.parametrize("searched_name, expected_entry",
                         [("Cierra", ["Cierra", "Vega", "39", "cierra@example.com", "10000", "Insurance"]),
                          ("Alden", ["Alden", "Cantrell", "45", "alden@example.com", "12000", "Compliance"]),
                          ("Kierra", ["Kierra", "Gentry", "29", "kierra@example.com", "2000", "Legal"])])
def test_search_entry(searched_name, expected_entry):
    search_box = driver.find_element_by_css_selector("#searchBox")

    search_box.send_keys(searched_name)

    # Search should return a single row with 6 data cells
    all_not_empty_rows = driver.find_elements_by_xpath(
        "//div[@class='rt-tr-group']/div/div[not(span) and not(div/span)]")

    assert not len(all_not_empty_rows) > 6

    iterator = 0
    for cell in all_not_empty_rows:
        assert cell.text == expected_entry[iterator]
        iterator += 1
