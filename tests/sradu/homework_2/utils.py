from typing import List
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


def wait_and_click(session, by, locator):
    WebDriverWait(session, 5).until(EC.element_to_be_clickable((by, locator))).click()


def wait_until_all_elements_visible(session, by, locator) -> List[WebElement]:
    return WebDriverWait(session, 5).until(EC.visibility_of_all_elements_located((by, locator)))
