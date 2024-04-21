import pytest

import constants

from selenium.webdriver import Chrome


@pytest.fixture(autouse=True)
def driver():
    driver = Chrome()
    driver.get(constants.URL_HOST)

    driver.implicitly_wait(3)

    yield driver

    # tear down
    driver.quit()
