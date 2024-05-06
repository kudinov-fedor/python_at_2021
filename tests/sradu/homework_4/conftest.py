from selenium.webdriver import Chrome
from tests.sradu.homework_4.constants import HOST
from selenium.webdriver.common.action_chains import ActionChains
import pytest


@pytest.fixture
def driver():
    driver = Chrome()
    driver.get(HOST)
    yield driver
    driver.quit()


@pytest.fixture
def action_chains(driver):
    return ActionChains(driver)
