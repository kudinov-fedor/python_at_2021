import pytest
from selenium.webdriver import Chrome
from tests.sradu.homework_4.constants import HOST


@pytest.fixture
def driver():
    driver = Chrome()
    driver.get(HOST)
    yield driver
    driver.quit()
