from typing import List

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.remote.webdriver import WebDriver

from magento_softwaretesting_board import config
from .comp import Cart, ProductItem


class BasePage:

    URL = config.HOST

    def __init__(self, session: WebDriver):
        self.session = session

    def open(self):
        self.session.get(self.URL)
        return self

    def element_is_present(self, *locator):
        try:
            return self.session.find_element(*locator)
        except NoSuchElementException:
            return False

    def get_cart(self) -> "Cart":
        # from .comp import Cart
        el = self.session.find_element(By.CSS_SELECTOR, ".action.showcart")
        return Cart(el)


class HomePage(BasePage):

    def user_logged_in(self) -> bool:
        el = self.element_is_present(By.CSS_SELECTOR, ".greet.welcome .logged-in")
        return el and "Welcome" in el.text

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

    def get_products(self) -> List["ProductItem"]:
        # from .comp import ProductItem

        el_loc = By.CSS_SELECTOR, "div.block-products-list li"
        return [ProductItem(el) for el in self.session.find_elements(*el_loc)]


class LoginPage(BasePage):

    def login(self, login=config.LOGIN, password=config.PASSWORD):
        self.session.find_element(By.CSS_SELECTOR, ".header.links li.authorization-link").click()
        self.session.find_element(By.CSS_SELECTOR, "#email").send_keys(login)
        self.session.find_element(By.CSS_SELECTOR, "#pass").send_keys(password)

        self.session.find_element(By.CSS_SELECTOR, "#send2").click()

        # wait until login
        home_page = HomePage(self.session)
        Wait(self.session, 3).until(lambda driver: home_page.user_logged_in())
        return home_page
