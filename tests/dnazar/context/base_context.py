from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BaseContext:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self, url: str):
        self.driver.get(url)
        return self

    def fill_field(self, field: WebElement, value: str):
        field.send_keys(value)
        return self

    def click_button(self, button: WebElement):
        button.click()
        return self

    def verify_element_contains_text(self, element: WebElement, expected: str):
        assert expected in element.text
        return self

    def verify_element_is_enabled(self, element: WebElement, expected: bool):
        actual = False if element.get_attribute("disabled") == 'true' else True
        assert expected == actual
        return self
