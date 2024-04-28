from selenium.webdriver.common.by import By


class LoginPageLoc:
    # TXT_USERNAME = (By.ID, "user-name")
    TXT_USERNAME = (By.XPATH, "//*[@id='user-name']")
    # TXT_PASSWORD = (By.ID, "password")
    TXT_PASSWORD = (By.XPATH, "//*[@id='password']")
    # BTN_LOGIN = (By.ID, "login-button")
    BTN_LOGIN = (By.XPATH, "//*[@id='login-button']")


class ProductsPageLoc:
    # LST_ITEMS = (By.CSS_SELECTOR, ".inventory_list .inventory_item")
    LST_ITEMS = (By.XPATH, "//*[contains(@class, 'inventory_list')]//*[contains(@class, 'inventory_item_description')]")
    # BTN_ADD_TO_CART = (By.XPATH, ".//*[@class='pricebar']//button")
    BTN_ADD_TO_CART = (By.CSS_SELECTOR, ".pricebar button")


class CartItemsLoc:
    # IMG_CART = (By.ID, "shopping_cart_container")
    IMG_CART = (By.XPATH, "//*[@id='shopping_cart_container']")
    # IMG_CART_BADGE = (By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
    IMG_CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    # LST_CART_ITEMS = (By.CSS_SELECTOR, ".cart_list .cart_item")
    LST_CART_ITEMS = (By.XPATH, ".//*[@class='cart_item']")
    # BTN_REMOVE_SECOND_ITEM = (By.ID, "remove-sauce-labs-fleece-jacket")
    BTN_REMOVE_SECOND_ITEM = (By.XPATH, "//*[@id='remove-sauce-labs-fleece-jacket']")
    # BTN_CHECKOUT = (By.ID, "checkout")
    BTN_CHECKOUT = (By.XPATH, "//*[@id='checkout']")


class InformationPageLoc:
    # TXT_FIRST_NAME = (By.ID, "first-name")
    TXT_FIRST_NAME = (By.XPATH, "//*[@id='first-name']")
    # TXT_LAST_NAME = (By.ID, "last-name")
    TXT_LAST_NAME = (By.XPATH, "//*[@id='last-name']")
    # TXT_POSTAL_CODE = (By.ID, "postal-code")
    TXT_POSTAL_CODE = (By.XPATH, "//*[@id='postal-code']")
    # BTN_CONTINUE = (By.ID, "continue")
    BTN_CONTINUE = (By.XPATH, "//*[@id='continue']")


class OverviewPageLoc:
    # TXT_ITEM_PRICE = (By.XPATH, "//*[contains(@class, 'inventory_item_price')]")
    TXT_ITEM_PRICE = (By.CSS_SELECTOR, ".inventory_item_price")
    # TXT_ITEM_TOTAL = (By.XPATH, "//*[contains(@class, 'summary_subtotal_label')]")
    TXT_ITEM_TOTAL = (By.CSS_SELECTOR, ".summary_subtotal_label")
    # BTN_FINISH = (By.ID, "finish")
    BTN_FINISH = (By.XPATH, "//*[@id='finish']")


class SuccessPageLoc:
    # BTN_BACK_HOME = (By.ID, "back-to-products")
    BTN_BACK_HOME = (By.XPATH, "//*[@id='back-to-products']")
