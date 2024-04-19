from selenium.webdriver.common.by import By


class LoginPage:
    """Login page locators"""
    # before-> (By.ID, "user-name")
    TXT_LOGIN_INPUT = (By.CSS_SELECTOR, "#user-name")
    # before-> (By.ID, "password")
    TXT_PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    # before-> (By.ID, "login-button")
    BTN_SUBMIT = (By.XPATH, "//*[@id='login-button']")


class LandingPage:
    """Landing page"""
    # before-> (By.CSS_SELECTOR, ".inventory_list .inventory_item")
    TABLE_PRODUCT_ITEMS = (By.XPATH, "//*[contains(@class,'inventory_list')]/*[contains(@class,'inventory_item')]")
    # before-> (By.XPATH, ".//*[@class='pricebar']//button")
    BTN_ADD_TO_CART = (By.CSS_SELECTOR, ".pricebar button")
    # before-> (By.ID, "shopping_cart_container")
    BTN_CART_LOCATE = (By.XPATH, "//*[@id='shopping_cart_container']")
    # before-> (By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
    TXT_CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")


class CartPage:
    """Cart page"""
    # before-> (By.CSS_SELECTOR, ".cart_list .cart_item")
    TABLE_ITEMS_IN_CART = (By.XPATH, "//*[contains(@class,'cart_list')]/*[@class='cart_item']")
    # before-> (By.CSS_SELECTOR, ".btn_secondary.btn_small.cart_button")
    BTN_REMOVE_FROM_CART = (By.XPATH, "//*[contains(@class,'btn_secondary')][contains(@class,'btn_small')]"
                                      "[contains(@class,'cart_button')]")
