from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains as AC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def action(self):
        return AC(self.driver)

    def double_click(self, locator):
        double_click_button = self.driver.find_element(*locator)
        self.action().double_click(on_element=double_click_button).perform()

    def right_click(self, locator):
        right_click_button = self.driver.find_element(*locator)
        self.action().context_click(on_element=right_click_button).perform()

    def left_click(self, locator):
        click_me_button = self.driver.find_element(*locator)
        click_me_button.click()

    def fill_field(self, locator, text):
        full_name_field = self.driver.find_element(*locator)
        full_name_field.clear()
        full_name_field.send_keys(text)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def scroll_down_page(self):
        self.driver.execute_script("window.scrollTo(0, 500);")
