from selenium.webdriver import Chrome
import pytest


@pytest.fixture()
def driver():
    driver = Chrome()
    driver.implicitly_wait(3)

    yield driver

    # tear down
    driver.quit()
