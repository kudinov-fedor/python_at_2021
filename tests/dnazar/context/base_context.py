from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BaseContext:
    def __init__(self, driver: WebDriver):
        self.alert = None
        self.driver = driver

    def open_page(self, url: str):
        self.driver.get(url)
        return self

    def switch_to_alert(self):
        for i in range(3):
            sleep(1)
            try:
                self.alert = self.driver.switch_to.alert
                break
            except:
                pass
        else:
            raise AssertionError("There are no alerts")
        return self

    def accept_alert(self):
        self.alert.accept()
        return self

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self

    def fill_field(self, field: WebElement, value: str):
        field.send_keys(value)
        return self

    def clear_field(self, field: WebElement):
        field.send_keys(Keys.CONTROL, 'a')
        field.send_keys(Keys.BACKSPACE)
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

    def verify_alert_text(self, expected: str):
        assert self.alert.text == expected
        return self
