from tests.yana_pokulita.HW4_DemoQA.page.base_page import BasePage
from tests.yana_pokulita.locators import CartLocators


class CheckoutCompletePage(BasePage):

    def back_to_products(self):
        self.click(*CartLocators.BackHomeBtn)
