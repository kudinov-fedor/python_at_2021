from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait


class BasePage:
    HOST = "https://demoqa.com"
    URL = ""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    def browser_name(self):
        return self.driver.capabilities["browserName"]

    @property
    def platform_name(self):
        return self.driver.capabilities["platformName"]

    @property
    def window_size(self):
        return self.driver.get_window_size()

    def open(self):
        self.driver.get(self.HOST + self.URL)
        return self.on_load

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

    @property
    def on_load(self):
        self.wait.until(EC.url_contains(self.URL))
        return self

    @property
    def wait(self) -> Wait:
        return Wait(self.driver, 10)

    def scroll_down(self):
        scroll_down = self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        return self

    def scroll_up(self):
        scroll_up = self.driver.execute_script("window.scrollTo(0,-document.body.scrollHeight)")
        return self
