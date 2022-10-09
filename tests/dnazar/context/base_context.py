from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC


class BaseContext:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self, url: str):
        self.driver.get(url)
        return self

    def switch_to_alert(self, wait_time: int = 0):
        WebDriverWait(self.driver, wait_time).until(EC.alert_is_present())
        return self.driver.switch_to.alert

    def accept_alert(self, alert: Alert):
        alert.accept()
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

    def verify_alert_text(self, alert: Alert, expected: str):
        assert alert.text == expected
        return self
