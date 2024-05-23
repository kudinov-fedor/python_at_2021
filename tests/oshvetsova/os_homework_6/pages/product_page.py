from selenium.webdriver.remote.webelement import WebElement
from .base_page import BasePage
from .locators import *
from .base_element import PageElement, SideNavigationElement


class ProductList(PageElement):
    def find_products(self) -> list[WebElement]:
        return self.find_elements(*ProductPageLocator.PRODUCT_LIST)

    def add_to_cart(self) -> None:
        self.find_element(*ProductPageLocator.BTN_ADD_TO_CART).click()


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def products_list(self) -> list[ProductList]:
        return [ProductList(product) for product in self.find_elements(*ProductPageLocator.PRODUCT_LIST)]

    def get_cart_link(self)-> WebElement:
        return self.driver.find_element(*ShoppingCart.LNK_CART)

    def open_cart(self):
        from tests.oshvetsova.os_homework_6.pages.cart_page import CartPageItem
        self.get_cart_link().click()
        return CartPageItem(self.driver)

    def logout_from_system(self) -> 'LogInPage':
        from tests.oshvetsova.os_homework_6.pages.login_page import LogInPage
        side_navigation = SideNavigationElement(self.get_side_navigation())
        side_navigation.click()
        side_navigation.click_logout_button()
        return LogInPage(self.driver)
