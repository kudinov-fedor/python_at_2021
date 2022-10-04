from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def action(self):
        return AC(self.driver)

    def double_click(self, locator):
        element = self.driver.find_element(*locator)
        self.action().double_click(on_element=element).perform()

    def right_click(self, locator):
        element = self.driver.find_element(*locator)
        self.action().context_click(on_element=element).perform()

    def left_click(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def fill_field(self, locator, text):
        field = self.driver.find_element(*locator)
        field.clear()
        field.send_keys(text)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def scroll_down_page(self):
        self.driver.execute_script("window.scrollTo(0, 500);")

    def wait_until_all_displayed(self, locator):
        WebDriverWait(driver=self.driver, timeout=5).\
            until(EC.presence_of_all_elements_located(locator))

    def check_element_is_disabled(self, locator):
        return False if self.find_element(*locator).get_attribute("disabled") == "true" else True
