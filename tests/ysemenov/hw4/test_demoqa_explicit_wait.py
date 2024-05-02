from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from tests.ysemenov.hw4.locators import DynamicPage
from tests.ysemenov.hw4.conftest import HOST
from tests.ysemenov.hw4.utils import wait_for_element


def test_button_enabled(session):
    session.get(HOST + "dynamic-properties")
    driver_wait = Wait(session, 5)
    driver_wait.until(EC.element_to_be_clickable(DynamicPage.BTN_ENABLED))
    assert session.find_element(*DynamicPage.BTN_ENABLED).is_enabled()


def test_button_color_changed(session):
    session.get(HOST + "dynamic-properties")
    wait_for_element(session, DynamicPage.BTN_COLOR, 5)


def test_button_visible(session):
    session.get(HOST + "dynamic-properties")
    wait_for_element(session, DynamicPage.BTN_VISIBLE, 6)
