from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait

from magento_softwaretesting_board.pageobject.page import BasePage, LoginPage
from magento_softwaretesting_board.pageobject.comp import ProductItem


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
        el_loc = By.CSS_SELECTOR, "div.block-products-list li"
        return [ProductItem(el) for el in self.session.find_elements(*el_loc)]
