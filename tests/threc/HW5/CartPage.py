from selenium.webdriver.common.by import By

from tests.threc.HW5.BasePage import BasePage


class CartPage(BasePage):
    def get_cart_item_name(self):
        return self.find_element_by(By.CSS_SELECTOR, ".cart_item .inventory_item_name").text

    def get_cart_badge_count(self):
        cart_badge = self.find_element_by(By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
        return cart_badge.text
