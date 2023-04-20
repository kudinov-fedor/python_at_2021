from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from magento_softwaretesting_board import config
from magento_softwaretesting_board.pageobject.page import BasePage


class LoginPage(BasePage):

    EXPLICIT_WAIT = config.EXPLICIT_WAIT

    def login(self, login=config.LOGIN, password=config.PASSWORD):
        from magento_softwaretesting_board.pageobject.page import HomePage  # lazy import to avoid cyclic import

        self.session.find_element(By.CSS_SELECTOR, "#email").send_keys(login)
        self.session.find_element(By.CSS_SELECTOR, "#pass").send_keys(password)
        self.session.find_element(By.CSS_SELECTOR, "#send2").click()

        # wait until login
        home_page = HomePage(self.session)
        self.wait.until(lambda driver: home_page.user_logged_in())
        return home_page

    def wait_load(self):
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "li.greet.welcome"), "Default welcome msg!"))
        return self
