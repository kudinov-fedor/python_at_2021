from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests. oshvetsova. os_homework_4.conftest import HOST
from tests. oshvetsova. os_homework_4.locators import DynamicProperties


def test_button_enabled(session):
    session.get(HOST + "dynamic-properties")
    webdriver_wait = WebDriverWait(session, 5)
    webdriver_wait.until(EC.element_to_be_clickable(*DynamicProperties.BTN_TEMP_DISABLED))
    assert session.find_element(*DynamicProperties.BTN_TEMP_DISABLED).is_enabled()


def test_button_change(session):
    session.get(HOST + "dynamic-properties")
    WebDriverWait(session, 6).until(EC.presence_of_element_located(DynamicProperties.BTN_COLOR_DANGER))
    assert (session.find_element(*DynamicProperties.BTN_COLOR_DANGER).is_displayed())


def test_visible_after(session):
    session.get(HOST + "dynamic-properties")
    WebDriverWait(session, 6).until(EC.presence_of_element_located(DynamicProperties.BTN_VISIBLE_AFTER))
    visible_button = session.find_element(*DynamicProperties.BTN_VISIBLE_AFTER)
    assert visible_button.is_displayed()
