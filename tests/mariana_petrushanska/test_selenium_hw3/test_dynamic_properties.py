import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.color import Color
from selenium.webdriver.support import expected_conditions as EC
from tests.mariana_petrushanska.test_selenium_hw3.locators import DynamicProperties


@pytest.mark.usefixtures("open_dynamic_properties_page")
def test_disabled_button(session):
    WebDriverWait(session, 6).until(EC.element_to_be_clickable(DynamicProperties.BTN_DISABLED))
    disabled_button = session.find_element(*DynamicProperties.BTN_DISABLED)
    assert disabled_button.is_enabled()


@pytest.mark.usefixtures("open_dynamic_properties_page")
def test_button_color_change(session):
    WebDriverWait(session, 6).until(EC.presence_of_element_located(DynamicProperties.BTN_COLOR_CHANGE))
    changed_button = session.find_element(*DynamicProperties.BTN_COLOR_CHANGE)
    button_color = Color.from_string(changed_button.value_of_css_property("color")).hex
    assert button_color == '#dc3545'


@pytest.mark.usefixtures("open_dynamic_properties_page")
def test_visible_after_button(session):
    WebDriverWait(session, 6).until(EC.presence_of_element_located(DynamicProperties.BTN_VISIBLE_AFTER))
    appearing_button = session.find_element(*DynamicProperties.BTN_VISIBLE_AFTER)
    assert appearing_button.is_displayed()
