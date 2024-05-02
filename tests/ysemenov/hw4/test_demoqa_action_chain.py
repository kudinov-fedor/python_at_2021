from selenium.webdriver.common.action_chains import ActionChains as AC
from tests.ysemenov.hw4.locators import ButtonsPage, DroppablePage
from tests.ysemenov.hw4.conftest import HOST
from tests.ysemenov.hw4.utils import wait_for_element


def test_btn_dbl_click(session):
    session.get(HOST + "buttons")
    btn_double = wait_for_element(session, ButtonsPage.BTN_DBL_CLICK, 5)
    AC(session).double_click(btn_double).perform()
    message = wait_for_element(session, ButtonsPage.MSG_DBL_CLICK, 5).text
    assert message == "You have done a double click"


def test_btn_right_click(session):
    session.get(HOST + "buttons")
    btn_right = wait_for_element(session, ButtonsPage.BTN_RIGHT_CLICK, 5)
    AC(session).context_click(btn_right).perform()
    message = wait_for_element(session, ButtonsPage.MSG_RIGHT_CLICK, 5).text
    assert message == "You have done a right click"


def test_btn_dyn_click(session):
    session.get(HOST + "buttons")
    btn_dyn = wait_for_element(session, ButtonsPage.BTN_DYN_CLICK, 5)
    AC(session).click(btn_dyn).perform()
    message = wait_for_element(session, ButtonsPage.MSG_DYN_CLICK, 5).text
    assert message == "You have done a dynamic click"


def test_drag_and_drop(session):
    session.get(HOST + "droppable")
    drag_box = session.find_element(*DroppablePage.DRAG_BOX)
    drop_box = session.find_element(*DroppablePage.DROP_BOX)
    AC(session).drag_and_drop(drag_box, drop_box).perform()
    wait_for_element(session, DroppablePage.DROPPED_TEXT, 5)
