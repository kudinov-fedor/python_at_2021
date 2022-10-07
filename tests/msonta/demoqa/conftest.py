from selenium.webdriver import Chrome, ChromeOptions
import pytest


@pytest.fixture(scope="module")
def session():
    options = ChromeOptions()
    driver = Chrome(options=options)
    driver.implicitly_wait(2)
    driver.maximize_window()
    yield driver
    driver.quit()
