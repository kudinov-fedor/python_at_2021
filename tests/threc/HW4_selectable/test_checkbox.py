from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from tests.threc.HW4_selectable.conftest import HOST

LIST = [
    'home',
    'desktop',
    'notes',
    'commands',
    'documents',
    'workspace',
    'react',
    'angular',
    'veu',
    'office',
    'public',
    'private',
    'classified',
    'general',
    'downloads',
    'wordFile',
    'excelFile'
]


def test_checkbox_select_all(driver):
    driver.get(HOST + '/checkbox')
    driver.find_element(By.XPATH, "//label[@for='tree-node-home']").click()

    items = driver.find_elements(By.XPATH, "//span[contains(@class,'text-success')]")
    item_texts = [item.text for item in items]
    assert item_texts == LIST


def test_checkbox_select_several(driver):
    short_list = [
        'desktop',
        'notes',
        'commands'
    ]

    driver.get(HOST + '/checkbox')
    driver.find_element(By.CSS_SELECTOR, ".rct-option-expand-all").click()

    driver.find_element(By.XPATH, "//label[@for='tree-node-desktop']").click()

    items = driver.find_elements(By.XPATH, "//span[contains(@class,'text-success')]")
    item_texts = [item.text for item in items]
    assert item_texts == short_list


def test_expand(driver):
    driver.get(HOST + '/checkbox')
    driver.find_element(By.XPATH, "//button[contains(@aria-label,'Expand all')]").click()

    driver.find_element(By.XPATH, "//label[@for='tree-node-home']").click()

    scroll_origin = ScrollOrigin.from_viewport(10, 10)

    ActionChains(driver) \
        .scroll_from_origin(scroll_origin, 0, 200) \
        .perform()

    items = driver.find_elements(By.XPATH, "//span[contains(@class,'text-success')]")
    item_texts = [item.text for item in items]
    assert item_texts == LIST
