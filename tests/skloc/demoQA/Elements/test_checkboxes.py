import pytest
from selenium.webdriver import Chrome


@pytest.fixture(autouse=True)
def test_setup():
    global driver
    driver = Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/checkbox")
    yield
    driver.close()
    driver.quit()


def test_mark_all_collapsed():
    top_check_btn = driver.find_element_by_css_selector(".rct-checkbox")

    top_check_btn.click()

    results = driver.find_elements_by_css_selector("#result span")

    expected_msg = "You have selected : home desktop notes commands documents workspace react angular veu office " \
                   "public private classified general downloads wordFile excelFile"

    for result in results:
        assert expected_msg.__contains__(result.text) and result.is_displayed()


def test_mark_2nd_lvl_element():
    home_drop_down_btn = driver.find_element_by_css_selector(".rct-collapse-btn")

    home_drop_down_btn.click()

    desktop_checkbox = driver.find_element_by_xpath("//label[@for='tree-node-desktop']/span[@class='rct-checkbox']")
    desktop_checkbox.click()

    results = driver.find_elements_by_css_selector("#result span")
    expected_msg = "You have selected : desktop notes commands"
    home_checkbox_mark = driver.find_element_by_xpath(
        "//label[@for='tree-node-home']/span[@class='rct-checkbox']/*").get_attribute("class")
    desktop_checkbox_mark = driver.find_element_by_xpath(
        "//label[@for='tree-node-desktop']/span[@class='rct-checkbox']/*").get_attribute("class")

    assert "rct-icon-half-check" in home_checkbox_mark
    assert "rct-icon-check" in desktop_checkbox_mark
    for result in results:
        assert expected_msg.__contains__(result.text) and result.is_displayed()

def test_mark_single_element():
    expand_all_btn = driver.find_element_by_css_selector(".rct-option-expand-all")

    expand_all_btn.click()

    office_private_checkbox = driver.find_element_by_xpath("//label[@for='tree-node-office']/../..//label[@for='tree-node-private']/span[@class='rct-checkbox']")

    office_private_checkbox.click()

    expected_msg = "You have selected : private"
    results = driver.find_elements_by_css_selector("#result span")

    for result in results:
        assert expected_msg.__contains__(result.text) and result.is_displayed()


