from tests.yana_pokulita.HW4_DemoQA.page.base_page import BasePage
from tests.yana_pokulita.locators import CartLocators


class CheckoutOverviewPage(BasePage):

    def finish_order(self):
        self.driver.find_element(*CartLocators.FinishBtn).click()
