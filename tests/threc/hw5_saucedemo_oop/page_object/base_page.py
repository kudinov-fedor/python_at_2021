class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def click(button):
        return button.click()

    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_elements(self, by, locator):
        return self.driver.find_elements(by, locator)

    @staticmethod
    def text(label):
        return label.text
