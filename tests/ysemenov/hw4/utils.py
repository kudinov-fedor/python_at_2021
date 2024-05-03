from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def wait_for_element(session: WebDriver, locator: tuple[str, str], timeout: int):
    """Wait for an element to be located on the page.
    Uses session, locator constant and timeout in seconds.
    Shows error if the element was not found and TimeoutException was caught.
    """
    try:
        driver_wait = Wait(session, timeout)
        return driver_wait.until(EC.presence_of_element_located(locator))
    except TimeoutException:
        raise TimeoutException(f"Element with locator: {locator} was not found within {timeout} second(s) timeout.")
