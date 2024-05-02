import pytest
from selenium.common import TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from tests.ysemenov.hw4.locators import ButtonsPage, DroppablePage


HOST = "https://demoqa.com/"


@pytest.fixture(scope="function")
def session():
    session = Chrome()
    session.implicitly_wait(0.2)
    yield session
    session.quit()


def wait_for_element(session: WebDriver, locator: tuple[str, str], timeout: int):
    """Wait for an element to be located on the page.
    Uses session, locator constant and timeout in seconds.
    Shows error if the element was not found and TimeoutException was caught.
    """
    try:
        driver_wait = Wait(session, timeout)
        return driver_wait.until(EC.presence_of_element_located(locator))
    except TimeoutException:
        pytest.fail(f"Element with locator: {locator} was not found within {timeout} second(s) timeout.")


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
