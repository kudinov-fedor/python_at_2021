from selenium.webdriver.common.by import By


class LoginPageLoc:
    TXT_USERNAME = (By.CSS_SELECTOR, "#user-name")
    # TXT_USERNAME = (By.XPATH, "//*[@id='user-name']")
    TXT_PASSWORD = (By.CSS_SELECTOR, "#password")
    # TXT_PASSWORD = (By.XPATH, "//*[@id='password']")
    BTN_LOGIN = (By.CSS_SELECTOR, "#login-button")
    # BTN_LOGIN = (By.XPATH, "//*[@id='login-button']")
    LST_CREDS_UN = (By.CSS_SELECTOR, "#login_credentials")
    # LST_CREDS_UN = (By.XPATH, "//*[@id='login_credentials']")
    LST_CREDS_PWD = (By.CSS_SELECTOR, "div.login_password")
    # LST_CREDS_PWD = (By.XPATH, "//*div[@class='login_password']")


class LandingPageLoc:
    ITEMS_CONTAINER = (By.CSS_SELECTOR, "#inventory_container")
    LST_ITEMS = (By.CSS_SELECTOR, ".inventory_list .inventory_item")
    # LST_ITEMS = (By.XPATH, "//*[@class='inventory_list']/div")
    BTN_ADD_TO_CART = (By.CSS_SELECTOR, ".pricebar .btn_inventory")
    # BTN_ADD_TO_CART = (By.XPATH, ".//*[@class='pricebar']//*[contains(@class,'btn_inventory')]")
    LNK_OPEN_PRODUCT = (By.CSS_SELECTOR, "div.inventory_item_name")
    TXT_PRODUCT_PRICE = (By.CSS_SELECTOR, "div.inventory_item_price")
    LNK_CART = (By.CSS_SELECTOR, ".shopping_cart_link")
    # LNK_CART = (By.XPATH, "//*[@class='shopping_cart_link']")
    IMG_CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    # IMG_CART_BADGE = (By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")


class CartItemsLoc:
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    CART_CONTAINER = (By.CSS_SELECTOR, "#shopping_cart_container")
    # CART_CONTAINER = (By.XPATH, "//*[@id='shopping_cart_container']"
    IMG_CART_BADGE = (By.CSS_SELECTOR, "span.shopping_cart_badge")
    # IMG_CART_BADGE = (By.XPATH, "//*[@id='shopping_cart_container']/a/span[contains(@class, 'shopping_cart_badge')]")
    BTN_REMOVE = (By.CSS_SELECTOR, "button.cart_button")
    BTN_CHECKOUT = (By.CSS_SELECTOR, "button.checkout_button")
    BTN_CONTINUE_SHOPPING = (By.CSS_SELECTOR, "#continue-shopping")
    ITEM_QUANTITY = (By.CSS_SELECTOR, ".cart_quantity")


class SideMenuLoc:
    BTN_BURGER_MENU = (By.CSS_SELECTOR, "button#react-burger-menu-btn")
    # BTN_BURGER_MENU = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    LST_SIDE_MENU = (By.CSS_SELECTOR, "nav.bm-item-list")
    LNK_LOGOUT = (By.CSS_SELECTOR, ".bm-item-list #logout_sidebar_link")
    # LNK_LOGOUT = (By.XPATH, "//*[contains(@class,'bm-item-list')]//*[@id='logout_sidebar_link']")


class OrderSubmitLoc:
    INPT_FIRST_NAME = (By.CSS_SELECTOR, "input#first-name.form_input")
    INPT_LAST_NAME = (By.CSS_SELECTOR, "input#last-name.form_input")
    INPT_POSTAL_CODE = (By.CSS_SELECTOR, "input#postal-code.form_input")
    BTN_CONTINUE = (By.CSS_SELECTOR, ".submit-button #continue")
    BTN_CANCEL = (By.CSS_SELECTOR, ".cart_cancel_link #cancel")


class CheckoutLoc:
    LST_CART_PRODUCTS = (By.CSS_SELECTOR, ".cart_list[data-test='cart-list']")
    BTN_FINISH = (By.CSS_SELECTOR, "button#finish.cart_button")
    BTN_CANCEL = (By.CSS_SELECTOR, "button#cancel.cart_cancel_link")


class CheckoutCompleteLoc:
    COMPLETE_CONTAINER = (By.CSS_SELECTOR, "#checkout_complete_container")
    BTN_BACK_HOME = (By.CSS_SELECTOR, "button#back-to-products")
