from selenium.webdriver.remote.webelement import WebElement
from tests.ysemenov.hw6.pages.base_page import BasePage, BaseElement
from tests.ysemenov.hw6.locators import LocatorsCartPage


class CartPageItem(BaseElement):

    def __init__(self, web_element: WebElement):
        super().__init__(web_element)

    def remove_from_cart(self):
        self.find_element(*LocatorsCartPage.BTN_REMOVE_FROM_CART).click()


class CartPage(BasePage):

    @property
    def items_in_cart(self) -> list[BaseElement]:
        elements = self.find_elements(*LocatorsCartPage.LST_CART_ITEMS)
        return [CartPageItem(element.element) for element in elements]

    def click_checkout(self):
        from tests.ysemenov.hw6.pages.checkout_page import CheckoutPage
        self.click_by_locator(*LocatorsCartPage.BTN_CHECKOUT)
        return CheckoutPage(self.driver)

    def remove_from_cart(self, product: BaseElement):
        CartPageItem(product.element).remove_from_cart()

    def click_continue_shopping(self):
        from tests.ysemenov.hw6.pages.inventory_page import InventoryPage
        self.click_by_locator(*LocatorsCartPage.BTN_CONTINUE_SHOPPING)
        return InventoryPage(self.driver)
