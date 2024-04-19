import time

from selenium.webdriver import Chrome

import pytest
from selenium.webdriver.common.by import By

from tests.threc.HW4_buttons import costants


@pytest.fixture()
def driver():
    driver = Chrome()
    driver.get(costants.URL_WINDOWS)
    driver.maximize_window()

    driver.implicitly_wait(4)

    yield driver

    # tear down
    driver.quit()


def test_new_tab(driver):
    driver.find_element(By.ID, "tabButton").click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url in costants.NEW_TAB_URL

    msg = driver.find_element(By.ID, "sampleHeading").text
    assert msg in costants.TEXT

    driver.close()


def test_new_window(driver):
    driver.find_element(By.ID, "windowButton").click()
    driver.switch_to.window(driver.window_handles[-1])
    assert driver.current_url in costants.NEW_TAB_URL

    msg = driver.find_element(By.ID, "sampleHeading").text
    assert msg in costants.TEXT

    driver.close()


def test_alert(driver):
    driver.find_element(By.ID, "messageWindowButton").click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    msg = driver.find_element(By.PARTIAL_LINK_TEXT, "Knowledge").text
    assert msg in costants.WINDOW_MSG
    driver.close()
