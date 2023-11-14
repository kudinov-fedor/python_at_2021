import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.mizo.constants import HOST2


def test_create_and_update_new_record(driver):
    driver.get(HOST2 + "/webtables")
    add_button = driver.find_element(By.CSS_SELECTOR, "#addNewRecordButton")
    add_button.click()
    registration_modal = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#registration-form-modal")))
    assert registration_modal.is_displayed()

    first_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#firstName")))
    first_name.send_keys("Mariia")
    last_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#lastName")))
    last_name.send_keys("Selenium")
    email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#userEmail")))
    email.send_keys("marichka@gmail.com")
    age = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#age")))
    age.send_keys("22")
    salary = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#salary")))
    salary.send_keys("1000")
    department = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#department")))
    department.send_keys("Washington Local")

    submit_button = driver.find_element(By.CSS_SELECTOR, "#submit")
    submit_button.click()

    table = driver.find_element(By.XPATH, "//div[@class='ReactTable -striped -highlight']")
    assert table.is_displayed()
    table_text = table.text
    assert "Selenium" in table_text


def test_edit_button(driver):
    driver.get(HOST2 + "/webtables")
    edit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#edit-record-1")))
    assert edit_button.is_displayed()
    edit_button.click()
    edited_salary = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#salary")))
    edited_salary.send_keys("3000")
    submit_button = driver.find_element(By.CSS_SELECTOR, "#submit")
    submit_button.click()
    table = driver.find_element(By.XPATH, "//div[@class='ReactTable -striped -highlight']")
    assert table.is_displayed()
    table_text = table.text
    assert "3000" in table_text


def test_delete_button(driver):
    driver.get(HOST2 + "/webtables")
    add_button = driver.find_element(By.CSS_SELECTOR, "#addNewRecordButton")
    add_button.click()
    registration_modal = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#registration-form-modal")))
    assert registration_modal.is_displayed()

    first_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#firstName")))
    first_name.send_keys("User")
    last_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#lastName")))
    last_name.send_keys("Deleted")
    email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#userEmail")))
    email.send_keys("user@gmail.com")
    age = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#age")))
    age.send_keys("22")
    salary = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#salary")))
    salary.send_keys("2000")
    department = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#department")))
    department.send_keys("None")

    submit_button = driver.find_element(By.CSS_SELECTOR, "#submit")
    submit_button.click()

    table = driver.find_element(By.XPATH, "//div[@class='ReactTable -striped -highlight']")
    assert table.is_displayed()
    table_text = table.text
    assert "Deleted" in table_text

    delete_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#delete-record-4")))
    assert delete_button.is_displayed()
    delete_button.click()
    table_text = table.text
    assert "Deleted" not in table_text


def test_search_box(driver):
    driver.get(HOST2 + "/webtables")
    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#searchBox")))
    search_box.send_keys("cie")
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, "//div[@class='ReactTable -striped -highlight']"), "Cierra")
    )
    table = driver.find_element(By.XPATH, "//div[@class='ReactTable -striped -highlight']")
    rows = table.find_elements(By.XPATH, ".//div[@class='rt-tr-group']")
    name_column = rows[0].find_element(By.XPATH, ".//div[contains(@class, 'rt-td')][1]")
    name = name_column.text
    assert name == "Cierra"
