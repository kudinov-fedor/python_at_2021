from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.remote.webdriver import WebDriver

from magento_softwaretesting_board import config


class BasePage:

    URL = config.HOST

    def __init__(self, session: WebDriver):
        self.session = session

    def open(self):
        self.session.get(self.URL)
        return self


class HomePage(BasePage):

    def user_logged_in(self) -> bool:
        try:
            return "Welcome" in self.session.find_element(By.CSS_SELECTOR, ".greet.welcome .logged-in").text
        except NoSuchElementException:
            return False

    def click_login(self):
        assert not self.user_logged_in()
        self.session.find_element(By.CSS_SELECTOR, ".header.links li.authorization-link").click()
        return LoginPage(self.session)

    def click_logout(self):
        assert self.user_logged_in()
        self.session.find_element(By.CSS_SELECTOR, "button[data-action='customer-menu-toggle']").click()
        self.session.find_element(By.CSS_SELECTOR, ".authorization-link").click()

        Wait(self.session, 3).until_not(lambda driver: self.user_logged_in())
        return self

class LoginPage(BasePage):
    def login(self, login=config.LOGIN, password=config.PASSWORD):
        self.session.find_element(By.CSS_SELECTOR, ".header.links li.authorization-link").click()
        self.session.find_element(By.CSS_SELECTOR, "#email").send_keys(login)
        self.session.find_element(By.CSS_SELECTOR, "#pass").send_keys(password)

        # remember url to check it changed
        url = self.session.current_url
        self.session.find_element(By.CSS_SELECTOR, "#send2").click()

        # wait until login
        home_page = HomePage(self.session)
        Wait(self.session, 3).until(lambda driver: home_page.user_logged_in())
        return home_page
