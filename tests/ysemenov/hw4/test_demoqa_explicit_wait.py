import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from tests.ysemenov.hw4.locators import DynamicPage


HOST = "https://demoqa.com/dynamic-properties"


@pytest.fixture(scope="function")
def session():
    session = Chrome()
    session.implicitly_wait(0.2)
    yield session
    session.quit()


def test_button_enabled(session):
    session.get(HOST)
    driver_wait = Wait(session, 5)
    driver_wait.until(EC.element_to_be_clickable(DynamicPage.BTN_ENABLED))
    assert session.find_element(*DynamicPage.BTN_ENABLED).is_enabled()


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


def test_button_color_changed(session):
    session.get(HOST)
    wait_for_element(session, DynamicPage.BTN_COLOR, 5)


def test_button_visible(session):
    session.get(HOST)
    wait_for_element(session, DynamicPage.BTN_VISIBLE, 6)
