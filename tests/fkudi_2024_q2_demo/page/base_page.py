

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, locator, wait=0):
        return self.driver.find_element(by, locator)

    def find_elements(self, by, locator, wait=0):
        return self.driver.find_elements(by, locator)

    def click(self, by, locator, wait=0):
        self.find_element(by, locator, wait).click()
