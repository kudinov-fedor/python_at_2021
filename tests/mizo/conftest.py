import pytest
from selenium.webdriver import Chrome


@pytest.fixture()
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
