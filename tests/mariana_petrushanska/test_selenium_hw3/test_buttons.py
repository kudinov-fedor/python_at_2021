import pytest
from selenium.webdriver.common.action_chains import ActionChains as AC
from tests.mariana_petrushanska.test_selenium_hw3.locators import ButtonsPage
from tests.mariana_petrushanska.test_selenium_hw3 import constants


@pytest.mark.usefixtures("open_buttons_page")
def test_double_click_button(session):
    double_click_button = session.find_element(*ButtonsPage.BTN_DOUBLE_CLICK)
    AC(session).double_click(double_click_button).perform()
    received_text = session.find_element(*ButtonsPage.TXT_DOUBLE_CLICK).text
    assert received_text == constants.DOUBLE_CLICK_MESSAGE


@pytest.mark.usefixtures("open_buttons_page")
def test_right_click_button(session):
    right_click_button = session.find_element(*ButtonsPage.BTN_RIGHT_CLICK)
    AC(session).context_click(right_click_button).perform()
    received_text = session.find_element(*ButtonsPage.TXT_RIGHT_CLICK).text
    assert received_text == constants.RIGHT_CLICK_MESSAGE


@pytest.mark.usefixtures("open_buttons_page")
def test_click_dynamic_button(session):
    dynamic_button = session.find_element(*ButtonsPage.BTN_DYNAMIC_CLICK)
    AC(session).click(dynamic_button).perform()
    received_text = session.find_element(*ButtonsPage.TXT_DYNAMIC_CLICK).text
    assert received_text == constants.REGULAR_CLICK_MESSAGE
