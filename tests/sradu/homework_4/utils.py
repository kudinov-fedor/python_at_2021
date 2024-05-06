from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as Wait
from tests.sradu.homework_4.constants import DEFAULT_TIMEOUT


def find_element(driver, by, value, *, wait=DEFAULT_TIMEOUT, check=EC.visibility_of_element_located):
    return Wait(driver, wait).until(check((by, value)))


def wait_for_all_elements(driver, by, value) -> List[WebElement]:
    return Wait(driver, DEFAULT_TIMEOUT).until(EC.visibility_of_all_elements_located((by, value)))


def get_menu_item(driver: WebDriver, locator: tuple, text: str):
    elements = driver.find_elements(*locator)
    for element in elements:
        if text in element.text:
            return element

    raise RuntimeError(f"Element with {text} was not found")


def click_by_action_chains(element: WebElement):
    action_chains = ActionChains(element.parent)
    action_chains.pause(1).move_to_element(element).pause(1).click().perform()


def drag_and_drop_by_action_chains(driver, source_element: WebElement, target_element: WebElement):
    action_chains = ActionChains(driver)
    (action_chains.pause(1)
     .click_and_hold(source_element)
     .pause(1)
     .move_to_element(target_element)
     .pause(1)
     .release()
     .perform())


def scroll_to_element(driver: WebDriver, element: WebElement):
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
