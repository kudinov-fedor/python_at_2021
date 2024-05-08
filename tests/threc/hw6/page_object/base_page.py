from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)

    @classmethod
    def text(cls, label):
        return label.text

    def click(self, locator, timeout=0):
        """Clicks an element with waiting for it to be clickable."""

        try:
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            raise AssertionError(f"Timed out waiting for element to be clickable: {locator}")
