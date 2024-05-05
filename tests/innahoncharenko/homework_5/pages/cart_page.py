from tests.innahoncharenko.homework_5.pages.base_page import BasePage
from tests.innahoncharenko.homework_5.pages.locators import CartLocators
from tests.innahoncharenko.homework_5.pages.checkout_page import CheckoutPage


class CartPage(BasePage):
    # Will return Landing page
    def back_to_landing_page(self):
        self.click_element(CartLocators.CONTINUE_SHOPPING_BUTTON)
        from tests.innahoncharenko.homework_5.pages.landing_page import LandingPage
        return LandingPage(self.driver)

    # Will return Checkout page
    def goto_checkout(self):
        self.click_element(CartLocators.CHECKOUT_BUTTON)
        return CheckoutPage(self.driver)

    def get_items_number(self):
        return len(self.find_elements(CartLocators.CART_ITEMS))

    def remove_item(self, item_index):
        item = self.find_elements(CartLocators.CART_ITEMS)[item_index]
        item.find_element(*CartLocators.CART_ITEMS_REMOVE_BUTTON).click()
