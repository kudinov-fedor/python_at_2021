from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait

from magento_softwaretesting_board import config
from magento_softwaretesting_board.pageobject.page import BasePage


class LoginPage(BasePage):

    def login(self, login=config.LOGIN, password=config.PASSWORD):
        from magento_softwaretesting_board.pageobject.page import HomePage  # lazy import to avoid cyclic import

        self.session.find_element(By.CSS_SELECTOR, ".header.links li.authorization-link").click()
        self.session.find_element(By.CSS_SELECTOR, "#email").send_keys(login)
        self.session.find_element(By.CSS_SELECTOR, "#pass").send_keys(password)

        self.session.find_element(By.CSS_SELECTOR, "#send2").click()

        # wait until login
        home_page = HomePage(self.session)
        Wait(self.session, 3).until(lambda driver: home_page.user_logged_in())
        return home_page
