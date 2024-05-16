from selenium.webdriver.remote.webelement import WebElement
from tests.ysemenov.hw5.pages.base_page import BasePage
from tests.ysemenov.hw5.locators import LocatorsCartPage


class CartPage(BasePage):

    def get_items_in_cart(self) -> list[WebElement]:
        return self.find_elements(*LocatorsCartPage.LST_CART_ITEMS)

    def click_checkout(self):
        self.click_by_locator(*LocatorsCartPage.BTN_CHECKOUT)

    def remove_from_cart(self, product: WebElement):
        product.find_element(*LocatorsCartPage.BTN_REMOVE_FROM_CART).click()

    def click_continue_shopping(self):
        self.click_by_locator(*LocatorsCartPage.BTN_CONTINUE_SHOPPING)
