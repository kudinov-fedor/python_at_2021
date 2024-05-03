from typing import List
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


def wait_for_element(session, by, value):
    return WebDriverWait(session, 5).until(EC.element_to_be_clickable((by, value)))


def wait_until_all_elements_visible(session, by, value) -> List[WebElement]:
    return WebDriverWait(session, 5).until(EC.visibility_of_all_elements_located((by, value)))
