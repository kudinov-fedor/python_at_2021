import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def test_setup():
    global driver
    driver = Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/browser-windows")
    yield
    driver.close()
    driver.quit()


def test_open_new_tab():
    new_tab_btn = driver.find_element(By.CSS_SELECTOR, "#tabButton")

    new_tab_btn.click()

    new_tab = driver.window_handles[1]
    driver.switch_to.window(new_tab)

    new_tab_text = driver.find_element(By.CSS_SELECTOR, "#sampleHeading").text

    assert new_tab_text == "This is a sample page"
