from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.mizo.constants import HOST


def test_home(driver):
    driver.get(HOST + "/checkbox")
    el = driver.find_element(By.CSS_SELECTOR, "#tree-node-home")
    assert not el.is_selected()
    el = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".rct-checkbox")))
    el.click()
    status_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "result")))
    expected_text = ('You have selected : home desktop notes commands documents workspace '
                     'react angular veu office public private classified general '
                     'downloads wordFile excelFile')
    actual_text = status_element.text.replace('\n', ' ')
    assert expected_text == actual_text


def test_home_is_unselected(driver):
    driver.get(HOST + "/checkbox")
    el = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".rct-checkbox")))
    el.click()
    el = driver.find_element(By.CSS_SELECTOR, "#tree-node-home")
    assert el.is_selected()
    el = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".rct-checkbox")))
    el.click()
    el = driver.find_element(By.CSS_SELECTOR, "#tree-node-home")
    assert not el.is_selected()


def test_home_expanded(driver):
    driver.get(HOST + "/checkbox")
    el = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Toggle'][title='Toggle']")
    el.click()
    status_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//span[@class='rct-title'][text()='Desktop']")))
    assert status_element.text == "Desktop"


def test_desktop_expanded(driver):
    driver.get(HOST + "/checkbox")
    home_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Toggle'][title='Toggle']")
    if not home_button.is_selected():
        home_button.click()

    desktop_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='tree-node']/ol/li/ol/li[1]/span/button")))

    desktop_button.click()

    # Check if the "Notes" node is visible when "Desktop" is expanded
    notes_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//span[@class='rct-title'][text()='Notes']")))
    assert notes_element.text == "Notes"


def test_documents_expanded(driver):
    driver.get(HOST + "/checkbox")
    home_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Toggle'][title='Toggle']")
    if not home_button.is_selected():
        home_button.click()
    documents_button = driver.find_element(By.XPATH,
                                           "//*[@id='tree-node']/ol/li/ol/li[2]/span/button")
    documents_button.click()

    office_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                     "//span[@class='rct-title'][text()='Office']")))
    assert office_element.text == "Office"


def test_downloads_expanded(driver):
    driver.get(HOST + "/checkbox")
    home_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Toggle'][title='Toggle']")
    if not home_button.is_selected():
        home_button.click()
    downloads_button = driver.find_element(By.XPATH,
                                           "//*[@id='tree-node']/ol/li/ol/li[3]/span/button")
    downloads_button.click()
    word_file_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                        "//span[@class='rct-title'][text()='Word File.doc']")))
    assert word_file_element.text == "Word File.doc"


def scroll_down(driver):
    driver.get(HOST + "/checkbox")
    # Scroll down using JavaScript
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def test_expand_all(driver):
    driver.get(HOST + "/checkbox")
    expand_all_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Expand all' and @title='Expand all']")))
    assert expand_all_button.is_enabled()
    expand_all_button.click()

    expected_text = "Home, Desktop, Notes, Commands, Documents, WorkSpace, React, Angular, Veu, Office, Public, Private, Classified, General, Downloads, Word File.doc, Excel File.doc"
    actual_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='check-box-tree-wrapper']"))).text
    actual_text = actual_text.replace('\n', ', ')
    assert actual_text == expected_text

    assert actual_text


def test_collapse_all(driver):
    driver.get(HOST + "/checkbox")
    expand_all_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Expand all' and @title='Expand all']")))
    assert expand_all_button.is_enabled()
    expand_all_button.click()
    collapse_all_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Collapse all' and @title='Collapse all']")))
    collapse_all_button.click()
    expected_text = "Home"
    actual_text = driver.find_element(By.XPATH, "//div[@class='check-box-tree-wrapper']").text
    actual_text = actual_text.replace('\n', ' ')
    assert actual_text == expected_text
