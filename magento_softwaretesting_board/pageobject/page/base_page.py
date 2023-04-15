from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from magento_softwaretesting_board import config
from magento_softwaretesting_board.pageobject.comp import Cart


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
        el = self.session.find_element(By.CSS_SELECTOR, ".action.showcart")
        return Cart(el)
