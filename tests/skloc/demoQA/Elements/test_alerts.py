from time import sleep

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def test_setup():
    global driver
    driver = Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/alerts")
    yield
    driver.close()
    driver.quit()


def test_simple_alert():
    alert_btn = driver.find_element_by_css_selector("#alertButton")
    alert_btn.click()

    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()

    assert alert_text == "You clicked a button"


def test_delayed_alert():
    delayed_alert_btn = driver.find_element_by_css_selector("#timerAlertButton")
    delayed_alert_btn.click()

    wait = WebDriverWait(driver, 6)
    wait.until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()

    assert alert_text == "This alert appeared after 5 seconds"


def test_dismiss_alert():
    alert_btn = driver.find_element_by_css_selector("#confirmButton")
    alert_btn.click()

    alert = driver.switch_to.alert
    alert.dismiss()

    result = driver.find_element_by_css_selector("#confirmResult").text

    assert result == "You selected Cancel"


def test_prompt_alert():
    alert_btn = driver.find_element_by_css_selector("#promtButton")
    alert_btn.click()

    alert = driver.switch_to.alert
    alert.send_keys("Lorem ipsum")
    alert.accept()

    result = driver.find_element_by_css_selector("#promptResult").text

    assert result == "You entered Lorem ipsum"

