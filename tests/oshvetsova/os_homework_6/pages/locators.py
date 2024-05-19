from selenium.webdriver.common.by import By


class LogInPageLoc:

    USER_NAME = (By.CSS_SELECTOR, "#user-name")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    BTN_LOGIN = (By.CSS_SELECTOR, "#login-button")


class ProductPageLocator:

    PRODUCT_LIST = (By.CSS_SELECTOR, ".inventory_list .inventory_item")
    BTN_ADD_TO_CART = (By.CSS_SELECTOR, ".pricebar button")
    CART_CONTAINER = (By.CSS_SELECTOR, ".shopping_cart_container")
    CART_BADGE = (By.CSS_SELECTOR, "#shopping_cart_container > a.shopping_cart_badge")


class ShoppingCart:

    LNK_CART = (By.XPATH, "//*[@class='shopping_cart_link']")
    CART_LIST = (By.XPATH, ".//*[@class='cart_item']")
    BTN_REMOVE = (By.CSS_SELECTOR, "button.cart_button")
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//*[contains(@class, 'btn')][@data-test='continue-shopping']")


class SideNavigation:
    BTN_NAVIGATION_MENU = (By.CSS_SELECTOR, "button#react-burger-menu-btn")
    LOGOUT_BUTTON = (By.XPATH, "//*[@id='logout_sidebar_link']")
