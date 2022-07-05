from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def scroll_down(driver: WebDriver) -> None:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


def forced_click_element(driver: WebDriver, element: WebElement) -> None:
    driver.execute_script('arguments[0].click();', element)


def scroll_to_element(driver: WebDriver, element: WebElement) -> None:
    driver.execute_script("arguments[0].scrollIntoView();", element)


def create_session(driver_type="chrome"):
    if driver_type == "chrome":
        return Chrome()
    if driver_type == "firefox":
        return Firefox()
