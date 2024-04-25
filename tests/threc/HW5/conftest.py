from selenium.webdriver import Chrome

import pytest


@pytest.fixture()
def driver():
    driver = Chrome()
    driver.get('https://www.saucedemo.com/')
    yield driver

    driver.quit()
