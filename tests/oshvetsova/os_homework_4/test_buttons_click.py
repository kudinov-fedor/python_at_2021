import pytest
from selenium.webdriver.common.action_chains import ActionChains as AC
from tests. oshvetsova. os_homework_4.conftest import HOST
from tests. oshvetsova. os_homework_4.locators import Buttons


def test_double_click_button(session):
    session.get(HOST + "buttons")
    double_click = session.find_element(*Buttons.BTN_DOUBLE_CLICK_ME)
    AC(session).double_click(double_click).perform()
    double_click_text = session.find_element(*Buttons.TXT_DOUBLE_CLICK_ME).text
    assert double_click_text == "You have done a double click"


def test_right_click_button(session):
    session.get(HOST + "buttons")
    right_click = session.find_element(*Buttons.BTN_RIGHT_CLICK_ME)
    AC(session).context_click(right_click).perform()
    right_click_text = session.find_element(*Buttons.TXT_RIGHT_CLICK_ME).text
    assert right_click_text == "You have done a right click"


def test_click_me_button(session):
    session.get(HOST + "buttons")
    click_me = session.find_element(*Buttons.BTN_CLICK_ME)
    AC(session).click(click_me).perform()
    click_me_text = session.find_element(*Buttons.TXT_CLICK_ME).text
    assert click_me_text == "You have done a dynamic click"
