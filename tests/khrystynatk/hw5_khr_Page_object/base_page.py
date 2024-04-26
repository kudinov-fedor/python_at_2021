from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    from tests.khrystynatk.hw5_khr_Page_object.constants import HOST, USERNAME, PASSWORD

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        self.driver.get(BasePage.HOST)

    def get_url(self):
        return self.driver.current_url
