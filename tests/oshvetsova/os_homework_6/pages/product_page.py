from .base_page import BasePage
from .locators import *
from .base_element import PageElement, SideNavigationElement


class ProductList(PageElement):
    def find_products(self) -> list:
        elements = self.find_elements(*ProductPageLocator.PRODUCT_LIST)
        return elements

    def add_to_cart(self, index):
        self.find_products()[index].find_element(*ProductPageLocator.BTN_ADD_TO_CART).click()


class CartLink(PageElement):
    def open_cart(self):
        cart_link = self.find_element(*ShoppingCart.LNK_CART)
        cart_link.click()


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_list = ProductList(driver)
        self.cart_link = CartLink(driver)
        self.side_navigation = SideNavigationElement(driver)

    def add_product_to_cart(self, index):
        self.product_list.add_to_cart(index)
        return self

    def open_cart(self):
        self.cart_link.open_cart()
        return self

    def logout_from_system(self):
        self.side_navigation.open_navigation_menu()
        self.side_navigation.click_logout_button()

    def __getattr__(self, item):
        try:
            return self.__dict__[item]
        except KeyError:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{item}'")
