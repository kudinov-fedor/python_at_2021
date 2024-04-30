from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self, host):
        from tests.khrystynatk.pages.login_page import LoginPage

        self.driver.get(host)
        return LoginPage(self.driver)

    def get_url(self):
        return self.driver.current_url
