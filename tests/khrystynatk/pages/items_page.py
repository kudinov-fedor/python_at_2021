from tests.khrystynatk.pages.base_elements import ProductsElement
from tests.khrystynatk.pages.base_page import BasePage
from tests.khrystynatk.pages.locators1 import LandingPageLoc, SideMenuLoc


class ItemsPage(BasePage):

    def find_product_rows(self) -> list[ProductsElement]:
        elements = self.driver.find_elements(*LandingPageLoc.LST_ITEMS)
        return [ProductsElement(el) for el in elements]

    def logout_from_side_menu(self):
        from tests.khrystynatk.pages.login_page import LoginPage
        self.driver.find_element(*SideMenuLoc.BTN_BURGER_MENU).click()
        self.driver.find_element(*SideMenuLoc.LNK_LOGOUT).click()
        return LoginPage(self.driver)

    def go_to_cart(self):
        from tests.khrystynatk.pages.cart_page import CartPage

        cart_link = self.driver.find_element(*LandingPageLoc.LNK_CART)
        cart_link.click()
        return CartPage(self.driver)
