import pytest
from selenium.webdriver import Chrome


@pytest.fixture(autouse=True, scope="module")
def driver() -> Chrome:
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
