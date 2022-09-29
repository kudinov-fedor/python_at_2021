from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains as AC
from tests.msonta.demoqa.pages.base_page import BasePage


class ButtonsPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def action(self):
        return AC(self.driver)

    def double_click(self, locator):
        double_click_button = self.driver.find_element(*locator)
        self.action().double_click(on_element=double_click_button).perform()

    def right_click(self, locator):
        right_click_button = self.driver.find_element(*locator)
        self.action().context_click(on_element=right_click_button).perform()

    def regular_click(self, locator):
        click_me_button = self.driver.find_element(*locator)
        click_me_button.click()

    def get_double_click_msg(self, locator):
        double_click_msg = self.driver.find_element(*locator).text
        return double_click_msg

    def get_right_click_msg(self, locator):
        right_click_msg = self.driver.find_element(*locator).text
        return right_click_msg

    def get_regular_click_msg(self, locator):
        regular_click_msg = self.driver.find_element(*locator).text
        return regular_click_msg
