

class BasePage:

    HOST = "https://www.saucedemo.com"

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.HOST)

    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_elements(self, by, locator):
        return self.driver.find_elements(by, locator)
