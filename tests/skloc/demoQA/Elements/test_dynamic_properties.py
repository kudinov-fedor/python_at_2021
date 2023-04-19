import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def test_setup():
    global driver
    global wait
    driver = Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/dynamic-properties")
    wait = WebDriverWait(driver, 6)
    yield
    driver.close()
    driver.quit()


def test_disabled_btn():
    wait.until(EC.element_to_be_clickable((By.ID, "enableAfter")))
    disabled_btn = driver.find_element(By.ID, "enableAfter")
    assert disabled_btn.is_enabled()


def test_change_color_btn():

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-danger")))

    color_btn = driver.find_element(By.CSS_SELECTOR, ".text-danger")
    hex_color_btn = Color.from_string(color_btn.value_of_css_property("color")).hex

    assert hex_color_btn == "#dc3545"


def test_wait_for_btn():
    wait.until(EC.presence_of_element_located((By.ID, "visibleAfter")))
    visible_after_btn = driver.find_element(By.ID, "visibleAfter")
    assert visible_after_btn.is_displayed()
