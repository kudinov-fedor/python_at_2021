from selenium.webdriver.common.by import By

from .base_page import BasePage
from selenium.common import NoSuchElementException


# todo move to sepparate module, inherit form BaseElement
class CatalogProduct:

    def __init__(self, web_element):
        self.web_element = web_element

    def find_element(self, by, value):
        return self.web_element.find_element(by, value)

    def add_to_cart(self):
        self.find_element(By.XPATH, ".//*[@class='pricebar']//button").click()


class CatalogPage(BasePage):

    def get_products(self):
        """
        1. знайти елементи
        """
        elements = self.driver.find_elements(By.CSS_SELECTOR,
                                             ".inventory_list .inventory_item")
        return [CatalogProduct(e) for e in elements]

    def cart_indicator(self) -> int:
        """
        1. сказати юзеру скілки елементів в корзині    0, 4
        """
        cart = self.driver.find_element(By.ID, "shopping_cart_container")
        try:
            cart_badge = cart.find_element(By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
        except NoSuchElementException:
            return 0
        return int(cart_badge.text)

    def cart_indicator_present(self) -> bool:
        """
        1. сказати чи бачиш ти індикатор
        """
        cart = self.driver.find_element(By.ID, "shopping_cart_container")
        try:
            cart.find_element(By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
        except NoSuchElementException:
            return False
        return True
