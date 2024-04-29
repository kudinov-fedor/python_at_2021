from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_elem(self, button):
        button.click()

    def find_elem(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_elems(self, by, locator):
        return self.driver.find_elements(by, locator)
