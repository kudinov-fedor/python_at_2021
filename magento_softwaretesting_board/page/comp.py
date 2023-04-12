from typing import List

from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.common import NoSuchElementException


class BaseElement:

    def __init__(self, session: WebElement):
        self.session = session

    @property
    def parent(self):
        return self.session._parent

    def click(self, *locator):
        el = self.session
        if locator:
            el = self.session.find_element(*locator)
        el.click()
        return self

    def hover(self):
        AC(self.parent).move_to_element(self.session).perform()
        return self

    def element_is_present(self, *locator):
        # todo always searches from element,
        #  so if need global search, need to use specific xpath locator
        try:
            return self.session.find_element(*locator)
        except NoSuchElementException:
            return False


class Cart(BaseElement):

    LOCATOR = By.CSS_SELECTOR, ".action.showcart"

    def get_cart_dialog(self) -> "CartDialog":
        cart_el = self.session.find_element(*CartDialog.LOCATOR)
        if not cart_el.is_displayed():
            self.click()
        return CartDialog(cart_el)

    def items_count(self) -> int:
        res = self.session.find_element(By.CSS_SELECTOR, ".counter.qty .counter-number").text
        return int(res or 0)

    def cart_is_opened(self):
        return self.element_is_present(*CartDialog.LOCATOR)


class CartDialog(BaseElement):

    LOCATOR = (By.XPATH, "//*[@id='minicart-content-wrapper']")

    def is_active(self):
        return self.session.is_displayed()

    def close(self):
        self.click(By.CSS_SELECTOR, "#btn-minicart-close")

    def get_items(self) -> List["CartItem"]:
        return [CartItem(el) for el in self.session.find_elements(By.CSS_SELECTOR, "#mini-cart li")]

    def clean_cart(self):
        assert self.is_active()

        items = self.get_items()
        while items:
            curr_count = len(items)
            item = items.pop()
            item.delete()
            # wait untill curr count is reduced
            from selenium.webdriver.support.ui import WebDriverWait as Wait
            Wait(self.parent, 3).until_not(lambda _: self.is_active() and len(self.get_items()) == curr_count)
            items = self.get_items()

        return self


class CartItem(BaseElement):

    def edit(self):
        ...

    def delete(self):
        self.session.find_element(By.CSS_SELECTOR, "a.action.delete").click()

        submit_button = By.XPATH, '//*[contains(@class, "modals-wrapper")]'\
                                  '//button[contains(@class, "action-accept")]'
        Wait(self.parent, 3).until(EC.element_to_be_clickable(submit_button)).click()


class ProductItem(BaseElement):

    def add_to_cart(self):
        from .page import HomePage

        home_page = HomePage(self.parent)
        items_count = home_page.get_cart().items_count()

        self.hover()
        self.session.find_element(By.CSS_SELECTOR, "button.tocart").click()

        Wait(self.parent, 3).until(lambda session: home_page.get_cart().items_count() > items_count)

    def add_to_wishlist(self):
        ...
