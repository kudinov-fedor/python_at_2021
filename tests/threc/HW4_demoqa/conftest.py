import pytest
from selenium.webdriver.common.by import By

import constants

from selenium.webdriver import Chrome


@pytest.fixture(autouse=True)
def driver():
    driver = Chrome()
    driver.get(constants.URL_HOST)

    driver.find_element(By.ID, 'userName').send_keys(constants.FIRST_NAME)
    driver.find_element(By.ID, 'userEmail').send_keys(constants.USER_EMAIL)
    driver.find_element(By.ID, 'currentAddress').send_keys(constants.CURRENT_ADDRESS)
    driver.find_element(By.ID, 'permanentAddress').send_keys(constants.PERMANENT_ADDRESS)

    driver.implicitly_wait(3)

    yield driver

    # tear down
    driver.quit()
