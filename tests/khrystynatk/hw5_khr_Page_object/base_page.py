from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self, host):
        self.driver.get(host)

    def get_url(self):
        return self.driver.current_url
