from tests.innahoncharenko.homework_6.pages.base_page import BasePage
from tests.innahoncharenko.homework_6.pages.locators import CartLocators
from tests.innahoncharenko.homework_6.pages.locators import InventoryItemsLocators
from tests.innahoncharenko.homework_6.pages.item_page import ItemPage
from tests.innahoncharenko.homework_6.pages.cart_page import CartPage
from tests.innahoncharenko.homework_6.pages.cart_element import CartElement
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement


class Product:
    def __init__(self, web_driver, web_element):
        self.driver = web_driver
        self.element: WebElement = web_element

    @property
    def get_item_name(self):
        return self.element.find_element(*InventoryItemsLocators.INVENTORY_ITEM_NAME)

    def click_element_button(self):
        self.element.find_element(*InventoryItemsLocators.BUTTON).click()

    add_item_to_cart = click_element_button
    remove_item_from_cart = click_element_button

    # Will return Item Page
    def open_item(self):
        self.get_item_name.click()
        return ItemPage(self.driver)


class LandingPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.cart_element = CartElement(self.driver)

    # Will return Cart page
    def open_cart(self):
        return self.cart_element.open_cart_page()

    def get_items_in_cart_number(self):
        return self.cart_element.get_items_in_cart_number

    def get_items(self) -> list[Product]:
        result = []
        elements = self.find_elements(InventoryItemsLocators.INVENTORY_ITEMS)

        for element in elements:
            result.append(Product(self.driver, element))

        return result
