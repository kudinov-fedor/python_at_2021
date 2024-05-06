from selenium.webdriver import Chrome
from tests.sradu.homework_4.constants import HOST
import pytest


@pytest.fixture
def driver():
    driver = Chrome()
    driver.get(HOST)
    yield driver
    driver.quit()
