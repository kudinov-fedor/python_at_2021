from tests.mariana_petrushanska.test_selenium_hw4 import constants


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(constants.HOST)

    def get_items_number(self, items):
        number = len(items)
        return number
