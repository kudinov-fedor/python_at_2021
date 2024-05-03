

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_elements(self, by, locator):
        return self.driver.find_elements(by, locator)

    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)

    def click(self, by, locator):
        self.find_element(by, locator).click()
