from selenium.webdriver.remote.webdriver import WebDriver
from tests.msonta.demoqa import config
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tests.msonta.demoqa.pages.base_page import BasePage
from tests.msonta.demoqa.locators import ButtonPageLocators as locators
from time import sleep


class ButtonsPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver.get(config.HOST + "buttons")
        # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "#banner-eta-vanilla > div")))
        # WebDriverWait(driver, 5)
        self.action = AC(driver)
        self.double_click_msg = ""
        self.right_click_msg = ""
        self.click_me_msg = ""

    def double_click(self):
        double_click_button = self.driver.find_element(*locators.double_click_button)
        self.action.double_click(on_element=double_click_button).perform()
        self.double_click_msg = self.driver.find_element(*locators.double_click_msg)

    def right_click(self):
        right_click_button = self.driver.find_element(*locators.right_click_button)
        self.action.context_click(on_element=right_click_button).perform()
        self.right_click_msg = self.driver.find_element(*locators.right_click_msg)

    def regular_click(self):
        click_me_button = self.driver.find_element(*locators.click_me_button)
        click_me_button.click()
        self.click_me_msg = self.driver.find_element(*locators.click_me_msg)

