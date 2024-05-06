from selenium.webdriver.common.by import By


class LoginPage:
    """Login page locators"""
    TXT_LOGIN_INPUT = (By.CSS_SELECTOR, "#user-name")
    TXT_PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    BTN_SUBMIT = (By.XPATH, "//*[@id='login-button']")


class LandingPage:
    """Landing page"""
    TABLE_PRODUCT_ITEMS = (By.XPATH, "//*[contains(@class,'inventory_list')]/*[contains(@class,'inventory_item')]")
    BTN_ADD_TO_CART = (By.CSS_SELECTOR, ".pricebar button")
    BTN_CART_LOCATE = (By.XPATH, "//*[@id='shopping_cart_container']")
    TXT_CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")


class CartPage:
    """Cart page"""
    TABLE_ITEMS_IN_CART = (By.XPATH, "//*[contains(@class,'cart_list')]/*[@class='cart_item']")
    BTN_REMOVE_FROM_CART = (By.XPATH, ".//*[contains(@class,'btn_secondary')][contains(@class,'btn_small')]"
                                      "[contains(@class,'cart_button')]")
