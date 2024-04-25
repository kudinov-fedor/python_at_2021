
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        return self.driver.get('https://www.saucedemo.com/')

    def find_element_by(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_elements(self, by, locator):
        return self.driver.find_elements(by, locator)

    def click(self, by, locator):
        element = self.find_element_by(by, locator)
        element.click()

