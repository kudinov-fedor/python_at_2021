class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        self.find_element(locator).click()

    def get_current_url(self):
        return str(self.driver.current_url)