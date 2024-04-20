import pytest
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

EL1 = 'Cras justo odio'
EL2 = 'Dapibus ac facilisis in'
EL3 = 'Morbi leo risus'
EL4 = 'Porta ac consectetur ac'
ACTIVE_TAB = 'Grid'


@pytest.fixture()
def driver():
    driver = Chrome()
    driver.get('https://demoqa.com/selectable')

    driver.implicitly_wait(3)

    yield driver

    # tear down
    driver.quit()


def test_selectable_list(driver):
    driver.find_element(By.ID, "demo-tab-list")
    scroll_origin = ScrollOrigin.from_viewport(10, 10)

    ActionChains(driver) \
        .scroll_from_origin(scroll_origin, 0, 200) \
        .perform()

    driver.find_element(By.XPATH, "//*[@id='verticalListContainer']/li[1]").click()
    driver.find_element(By.XPATH, "//*[@id='verticalListContainer']/li[2]").click()
    driver.find_element(By.XPATH, "//*[@id='verticalListContainer']/li[3]").click()
    driver.find_element(By.XPATH, "//*[@id='verticalListContainer']/li[4]").click()

    el1 = driver.find_element(By.XPATH, "//li[1][contains(@class,'active list-group-item-action')]").text
    assert el1 in EL1

    el2 = driver.find_element(By.XPATH, "//li[2][contains(@class,'active list-group-item-action')]").text
    assert el2 in EL2

    el3 = driver.find_element(By.XPATH, "//li[3][contains(@class,'active list-group-item-action')]").text
    assert el3 in EL3

    el4 = driver.find_element(By.XPATH, "//li[4][contains(@class,'active list-group-item-action')]").text
    assert el4 in EL4

    driver.close()


def test_selectable_grid(driver):
    driver.find_element(By.ID, "demo-tab-grid").click()
    active = driver.find_element(By.XPATH, "//a[contains(@aria-selected,'true')]").text
    assert active in ACTIVE_TAB

    scroll_origin = ScrollOrigin.from_viewport(10, 10)

    ActionChains(driver) \
        .scroll_from_origin(scroll_origin, 0, 200) \
        .perform()

    driver.find_element(By.XPATH, "//*[@id='row1']/li[1]").click()
    driver.find_element(By.XPATH, "//*[@id='row1']/li[2]").click()
    driver.find_element(By.XPATH, "//*[@id='row1']/li[3]").click()
    driver.find_element(By.XPATH, "//*[@id='row2']/li[1]").click()

    el1 = driver.find_element(By.XPATH, "//li[1][contains(@class,'active list-group-item-action')]").text
    assert el1 in 'One'

    el2 = driver.find_element(By.XPATH, "//li[2][contains(@class,'active list-group-item-action')]").text
    assert el2 in 'Two'

    el3 = driver.find_element(By.XPATH, "//li[3][contains(@class,'active list-group-item-action')]").text
    assert el3 in 'Three'

    # не розумію як перейти на другий рядок ((((
    el4 = driver.find_element(By.XPATH, "//row[2]/li[1][contains(@class,'active list-group-item-action')]").text
    assert el4 in 'Four'

    driver.close()
