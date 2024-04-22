
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from tests.threc.HW4_selectable.conftest import HOST


def test_selectable_list(driver):
    driver.get(HOST + '/selectable')
    driver.find_element(By.ID, "demo-tab-list")
    scroll_origin = ScrollOrigin.from_viewport(10, 10)

    ActionChains(driver) \
        .scroll_from_origin(scroll_origin, 0, 200) \
        .perform()

    lines = driver.find_elements(By.CSS_SELECTOR, ".list-group-item")

    lines[0].click()
    line_text = lines[0].text
    assert line_text == "Cras justo odio"

    lines[1].click()
    line_text = lines[1].text
    assert line_text == "Dapibus ac facilisis in"

    lines[2].click()
    line_text = lines[2].text
    assert line_text == "Morbi leo risus"

    lines[3].click()
    line_text = lines[3].text
    assert line_text == "Porta ac consectetur ac"

    # selected = driver.find_elements(By.XPATH, "//ul[@id='verticalListContainer']/li[contains(@class, 'active')]")
    selected = driver.find_elements(By.XPATH, "//*[@id='verticalListContainer']/li[contains(@class, 'active')]")
    assert len(selected) == 4


def test_selectable_grid(driver):
    active_tab = 'Grid'
    driver.get(HOST + '/selectable')
    driver.find_element(By.ID, "demo-tab-grid").click()
    active = driver.find_element(By.XPATH, "//a[contains(@aria-selected,'true')]").text
    assert active in active_tab

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
    assert second_cell_text == "One"

    cells[1].click()
    second_cell_text = cells[1].text
    assert second_cell_text == "Two"

    cells[2].click()
    second_cell_text = cells[2].text
    assert second_cell_text == "Three"

    row_2 = rows[2]
    cells = row_2.find_elements(By.CSS_SELECTOR, ".list-group-item")

    cells[0].click()
    second_cell_text = cells[0].text
    assert second_cell_text == "Four"

    cells[1].click()
    second_cell_text = cells[1].text
    assert second_cell_text == "Five"

    # selected = driver.find_elements(By.XPATH, "//div/li[contains(@class, 'active')]")
    selected = driver.find_elements(By.XPATH, "//*[contains(@class, 'active')][contains(@class, 'list-group-item')]")
    assert len(selected) == 5
