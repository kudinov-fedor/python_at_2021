import pytest
from tests.khrystynatk.locators_for_alerts import LandingPage
from tests.khrystynatk.locators_for_alerts import Result
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

HOST = "https://demoqa.com"
SIMPLE_ALERT = "You clicked a button"
WAIT_ALERT = "This alert appeared after 5 seconds"
CONFIRM_BOX = "Do you confirm action?"
PROMPT_BOX = "Please enter your name"
ENTER_NAME = "Test_name"


@pytest.fixture
def driver():
    session = Chrome()
    session.implicitly_wait(0.5)
    session.maximize_window()
    yield session
    session.quit()


@pytest.fixture(autouse=True)
def open_page(driver):
    driver.get(HOST + "/alerts")


def test_alert(driver):
    """
    check alert text
    """

    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*LandingPage.alerts_wrapper))
    driver.find_element(*LandingPage.alert_button).click()
    alert = driver.switch_to.alert.text

    # check
    assert alert == SIMPLE_ALERT


def test_wait_alert(driver):
    """
    check wait alert text
    """

    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*LandingPage.alerts_wrapper))
    driver.find_element(*LandingPage.wait_alert_button).click()
    WebDriverWait(driver, 6).until(EC.alert_is_present())
    alert = driver.switch_to.alert.text

    # check
    assert alert == WAIT_ALERT


def test_decline_alert(driver):
    """
    - check alert text
    - check decline alert option
    - check decline alert result
    """

    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*LandingPage.alerts_wrapper))
    driver.find_element(*LandingPage.confirm_alert_button).click()

    # check alert text
    alert = driver.switch_to.alert
    assert alert.text == CONFIRM_BOX

    # check decline alert
    alert.dismiss()
    try:
        driver.switch_to.alert
    except NoAlertPresentException:
        print("Alert is closed")

    # check result text
    assert driver.find_element(*Result.confirm_alert_res).is_displayed()
    assert "Cancel" in driver.find_element(*Result.confirm_alert_res).text


def test_prompt_box(driver):
    """
    - check prompt box text
    - check prompt box input sent result
    """

    wrapper = driver.find_element(*LandingPage.alerts_wrapper)
    driver.execute_script("arguments[0].scrollIntoView();", wrapper)
    driver.find_element(*LandingPage.prompt_box_button).click()

    # check alert text
    alert = driver.switch_to.alert
    assert alert.text == PROMPT_BOX

    # check input sent result
    alert.send_keys(ENTER_NAME)
    alert.accept()
    assert driver.find_element(*Result.prompt_box_res).is_displayed()
    assert ENTER_NAME in driver.find_element(*Result.prompt_box_res).text
