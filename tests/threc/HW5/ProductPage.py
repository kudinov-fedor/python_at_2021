from selenium.webdriver.common.by import By
from tests.threc.HW5.BasePage import BasePage


class ProductPage(BasePage):
    def add_to_cart(self):
        items = self.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
        item = items[0].find_element_by(By.XPATH, ".//*[@class='pricebar']//button")
        item.click()

    def product_details(self):
        items = self.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
        item = items[0].find_element(By.XPATH, ".//*[@class='pricebar']//button")
        item.text()
