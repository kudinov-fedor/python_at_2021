import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

HOST = 'https://demoqa.com'
ACTIVE_TAB = 'Grid'


@pytest.mark.usefixture("driver")
def test_selectable_list(driver):
    driver.get(HOST + '/selectable')
    driver.find_element(By.ID, "demo-tab-list")
    scroll_origin = ScrollOrigin.from_viewport(10, 10)

    ActionChains(driver) \
        .scroll_from_origin(scroll_origin, 0, 200) \
        .perform()

    lines = driver.find_elements(By.CSS_SELECTOR, ".list-group-item")

    lines[0].click()
    first_line_text = lines[0].text
    assert first_line_text in "Cras justo odio"

    lines[1].click()
    first_line_text = lines[1].text
    assert first_line_text in "Dapibus ac facilisis in"

    lines[2].click()
    first_line_text = lines[2].text
    assert first_line_text in "Morbi leo risus"

    lines[3].click()
    first_line_text = lines[3].text
    assert first_line_text in "Porta ac consectetur ac"

    driver.close()


@pytest.mark.usefixture("driver")
def test_selectable_grid(driver):
    driver.get(HOST + '/selectable')
    driver.find_element(By.ID, "demo-tab-grid").click()
    active = driver.find_element(By.XPATH, "//a[contains(@aria-selected,'true')]").text
    assert active in ACTIVE_TAB

    scroll_origin = ScrollOrigin.from_viewport(10, 10)

    ActionChains(driver) \
        .scroll_from_origin(scroll_origin, 0, 200) \
        .perform()

    driver.find_element(By.CSS_SELECTOR, "#gridContainer")
    rows = driver.find_elements(By.CSS_SELECTOR, ".list-group")
    row_1 = rows[1]
    cells = row_1.find_elements(By.CSS_SELECTOR, ".list-group-item")

    cells[0].click()
    second_cell_text = cells[0].text
    assert second_cell_text in "One"

    cells[1].click()
    second_cell_text = cells[1].text
    assert second_cell_text in "Two"

    cells[2].click()
    second_cell_text = cells[2].text
    assert second_cell_text == "Three"

    row_2 = rows[2]
    cells = row_2.find_elements(By.CSS_SELECTOR, ".list-group-item")

    cells[0].click()
    second_cell_text = cells[0].text
    assert second_cell_text in "Four"

    cells[1].click()
    second_cell_text = cells[1].text
    assert second_cell_text in "Five"

    driver.close()
