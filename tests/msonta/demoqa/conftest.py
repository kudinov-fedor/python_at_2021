from selenium.webdriver import Chrome, ChromeOptions, Remote
import pytest
from tests.msonta.demoqa import config


@pytest.fixture(scope="module")
def session():
    options = ChromeOptions()
    driver = Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
