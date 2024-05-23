from tests.mariana_petrushanska.test_selenium_hw5.web_element import CartPageItem
from tests.mariana_petrushanska.test_selenium_hw5.base_page import BasePage
from tests.mariana_petrushanska.test_selenium_hw5.locators import CartItemsLoc


class CartPage(BasePage):

    @property
    def items_in_cart(self) -> list[CartPageItem]:
        items = self.find_elements(*CartItemsLoc.LST_CART_ITEMS)
        return [CartPageItem(item) for item in items]

    def checkout_btn_is_active(self) -> bool:
        return self.find_element(*CartItemsLoc.BTN_CHECKOUT).is_enabled()

    def go_to_checkout_page(self):
        self.find_element(*CartItemsLoc.BTN_CHECKOUT).click()
