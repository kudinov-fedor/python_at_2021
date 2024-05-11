from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    HOST = "https://www.saucedemo.com"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.HOST)
        return self

    def find_element(self, by: str, locator: str):
        return self.driver.find_element(by, locator)

    def find_elements(self, by: str, locator: str):
        return self.driver.find_elements(by, locator)

    def click(self, by: str, locator: str):
        return self.find_element(by, locator).click()

    def get_price(self,by: str, locator: str):
        return self.find_element(by, locator).text
