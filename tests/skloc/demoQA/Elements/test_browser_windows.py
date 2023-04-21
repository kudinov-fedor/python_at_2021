import pytest
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True, scope="function")
def test_setup(driver):
    driver.get("https://demoqa.com/browser-windows")


def test_open_new_tab(driver):
    new_tab_btn = driver.find_element(By.CSS_SELECTOR, "#tabButton")

    new_tab_btn.click()

    new_tab = driver.window_handles[-1]
    driver.switch_to.window(new_tab)

    new_tab_text = driver.find_element(By.CSS_SELECTOR, "#sampleHeading").text

    assert new_tab_text == "This is a sample page"
