from selenium.webdriver import Chrome, ChromeOptions
import pytest


@pytest.fixture()
def session():
    options = ChromeOptions()
    driver = Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
