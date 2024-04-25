from selenium.webdriver.common.by import By
from tests.threc.HW5.BasePage import BasePage


class LoginPage(BasePage):
    def login(self, login, password):
        self.driver.find_element_by(By.ID, 'user-name').send_keys(login)
        self.driver.find_element_by(By.ID, "password").send_keys(password)
        self.driver.click(By.ID, 'login-button')
