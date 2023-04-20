import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True, scope="function")
def test_setup(driver):
    driver.get("https://demoqa.com/alerts")


def test_simple_alert(driver):
    alert_btn = driver.find_element(By.CSS_SELECTOR, "#alertButton")
    alert_btn.click()

    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()

    assert alert_text == "You clicked a button"


def test_delayed_alert(driver):
    delayed_alert_btn = driver.find_element(By.CSS_SELECTOR, "#timerAlertButton")
    delayed_alert_btn.click()

    wait = WebDriverWait(driver, 6)

    alert = wait.until(EC.alert_is_present())
    alert_text = alert.text
    alert.accept()

    assert alert_text == "This alert appeared after 5 seconds"


def test_dismiss_alert(driver):
    alert_btn = driver.find_element(By.CSS_SELECTOR, "#confirmButton")
    alert_btn.click()

    alert = driver.switch_to.alert
    alert.dismiss()

    result = driver.find_element(By.CSS_SELECTOR, "#confirmResult").text

    assert result == "You selected Cancel"


def test_prompt_alert(driver):
    alert_btn = driver.find_element(By.CSS_SELECTOR, "#promtButton")
    alert_btn.click()

    alert = driver.switch_to.alert
    alert.send_keys("Lorem ipsum")
    alert.accept()

    result = driver.find_element(By.CSS_SELECTOR, "#promptResult").text

    assert result == "You entered Lorem ipsum"

