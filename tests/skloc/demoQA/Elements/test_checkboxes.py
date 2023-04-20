import pytest
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True, scope="function")
def test_setup(driver):
    driver.get("https://demoqa.com/checkbox")


def test_mark_all_collapsed(driver):
    top_check_btn = driver.find_element(By.CSS_SELECTOR, ".rct-checkbox")

    top_check_btn.click()

    results = driver.find_elements(By.CSS_SELECTOR, "#result span")

    expected_msg = "You have selected : home desktop notes commands documents workspace react angular veu office " \
                   "public private classified general downloads wordFile excelFile"

    for result in results:
        assert result.text in expected_msg and result.is_displayed()


def test_mark_2nd_lvl_element(driver):
    home_drop_down_btn = driver.find_element(By.CSS_SELECTOR, ".rct-collapse-btn")

    home_drop_down_btn.click()

    desktop_checkbox = driver.find_element(By.XPATH, "//label[@for='tree-node-desktop']/span[@class='rct-checkbox']")
    desktop_checkbox.click()

    results = driver.find_elements(By.CSS_SELECTOR, "#result span")
    expected_msg = "You have selected : desktop notes commands"
    home_checkbox_loc = "//label[@for='tree-node-home']/span[@class='rct-checkbox']/*"
    home_checkbox_mark = driver.find_element(By.XPATH, home_checkbox_loc).get_attribute("class")
    desktop_checkbox_locator = "//label[@for='tree-node-desktop']/span[@class='rct-checkbox']/*"
    desktop_checkbox_mark = driver.find_element(By.XPATH, desktop_checkbox_locator).get_attribute("class")

    assert "rct-icon-half-check" in home_checkbox_mark
    assert "rct-icon-check" in desktop_checkbox_mark
    for result in results:
        assert result.text in expected_msg and result.is_displayed()


def test_mark_single_element(driver):
    expand_all_btn = driver.find_element(By.CSS_SELECTOR, ".rct-option-expand-all")

    expand_all_btn.click()

    office_loc = "//label[@for='tree-node-office']/../..//label[@for='tree-node-private']/span[@class='rct-checkbox']"
    office_private_checkbox = driver.find_element(By.XPATH, office_loc)

    office_private_checkbox.click()

    expected_msg = "You have selected : private"
    results = driver.find_elements(By.CSS_SELECTOR, "#result span")

    for result in results:
        assert result.text in expected_msg and result.is_displayed()
