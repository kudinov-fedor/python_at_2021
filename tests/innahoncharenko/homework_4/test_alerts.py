import pytest
import time

from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait

from selenium.webdriver.common.action_chains import ActionChains as AC

URL = "https://demoqa.com/alerts"


def scroll_to_page_bottom(session):
    session.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.PAGE_DOWN)


@pytest.fixture
def open_session():
    session = Chrome()

    session.get(URL)

    yield session

    session.quit()


# alert button test
def test_alert_button(open_session):
    scroll_to_page_bottom(open_session)
    button = open_session.find_element(By.ID, "alertButton")
    AC(open_session).scroll_to_element(button).perform()
    button.click()

    alert = Wait(open_session, 1).until(EC.alert_is_present())
    assert "You clicked a button" == alert.text
    alert.accept()


# timer alert button test
def test_timer_alert_button(open_session):
    scroll_to_page_bottom(open_session)
    button = open_session.find_element(By.ID, "timerAlertButton")
    AC(open_session).scroll_to_element(button).perform()

    button.click()

    alert = Wait(open_session, 6).until(EC.alert_is_present())

    assert "This alert appeared after 5 seconds" == alert.text
    alert.accept()


# confirm box test
def test_confirm_box_confirm(open_session):
    scroll_to_page_bottom(open_session)
    button = open_session.find_element(By.ID, "confirmButton")
    AC(open_session).scroll_to_element(button).perform()

    button.click()

    alert = Wait(open_session, 1).until(EC.alert_is_present())

    assert "Do you confirm action?" == alert.text
    alert.accept()

    confirm_result = Wait(open_session, 1).until(EC.presence_of_element_located((By.ID, "confirmResult")))

    assert "You selected Ok" in confirm_result.text


def test_confirm_box_cancel(open_session):
    scroll_to_page_bottom(open_session)
    button = open_session.find_element(By.ID, "confirmButton")
    AC(open_session).scroll_to_element(button).perform()

    button.click()

    alert = Wait(open_session, 1).until(EC.alert_is_present())

    assert "Do you confirm action?" == alert.text
    alert.dismiss()

    confirm_result = Wait(open_session, 1).until(EC.presence_of_element_located((By.ID, "confirmResult")))

    assert "You selected Cancel" in confirm_result.text


# prompt tests
class PromptButtonLocators:
    BUTTON = (By.ID, "promtButton")
    RESULT = (By.ID, "promptResult")


def test_alerts_prompt_default_flow(open_session):
    scroll_to_page_bottom(open_session)

    button = open_session.find_element(*PromptButtonLocators.BUTTON)
    AC(open_session).scroll_to_element(button).perform()
    button.click()

    # default flow
    alert = Wait(open_session, 1).until(EC.alert_is_present())
    assert "Please enter your name" == alert.text
    alert.send_keys("Name")
    alert.accept()

    prompt_result = Wait(open_session, 1).until(EC.presence_of_element_located(PromptButtonLocators.RESULT))

    assert "You entered Name" in prompt_result.text


def test_alerts_prompt_accept_with_empty_value(open_session):
    scroll_to_page_bottom(open_session)

    button = open_session.find_element(*PromptButtonLocators.BUTTON)
    AC(open_session).scroll_to_element(button).perform()
    button.click()

    alert = Wait(open_session, 1).until(EC.alert_is_present())
    alert.accept()

    Wait(open_session, 1).until_not(EC.presence_of_element_located(PromptButtonLocators.RESULT))


def test_alerts_prompt_dismiss(open_session):
    scroll_to_page_bottom(open_session)

    button = open_session.find_element(*PromptButtonLocators.BUTTON)
    AC(open_session).scroll_to_element(button).perform()
    button.click()

    alert = Wait(open_session, 1).until(EC.alert_is_present())
    alert.dismiss()

    Wait(open_session, 1).until_not(EC.presence_of_element_located(PromptButtonLocators.RESULT))
