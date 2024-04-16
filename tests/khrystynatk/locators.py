from selenium.webdriver.common.by import By


class LoginPage:
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


class LandingPage:
    LST_ITEMS = (By.CSS_SELECTOR, ".inventory_list .inventory_item")
    # LST_ITEMS = (By.XPATH, "//*[@class='inventory_list']/div")
    BTN_ADD_TO_CART = (By.CSS_SELECTOR, ".pricebar .btn_inventory")
    # BTN_ADD_TO_CART = (By.XPATH, ".//*[@class='pricebar']//*[contains(@class,'btn_inventory')]")
    LNK_CART = (By.CSS_SELECTOR, ".shopping_cart_link")
    # LNK_CART = (By.XPATH, "//*[@class='shopping_cart_link']")
    IMG_CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    # IMG_CART_BADGE = (By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")


class CartItems:
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    # CART_ITEMS = (By.XPATH, "//*[@class = 'cart_item']")
    CART_CONTAINER = (By.CSS_SELECTOR, "#shopping_cart_container")
    # CART_CONTAINER = (By.XPATH, "//*[@id='shopping_cart_container']"
    IMG_CART_BADGE = (By.CSS_SELECTOR, "#shopping_cart_container > a.shopping_cart_badge")
    # IMG_CART_BADGE = (By.XPATH, "//*[@id='shopping_cart_container']/a/span[contains(@class, 'shopping_cart_badge')]")
    BTN_REMOVE_FIRST = (By.CSS_SELECTOR, "button#remove-sauce-labs-backpack")
    # BTN_REMOVE_FIRST = (By.XPATH, "//*[@id='remove-sauce-labs-backpack']")
    BTN_REMOVE_SECOND = (By.CSS_SELECTOR, "button#remove-sauce-labs-bike-light")
    # BTN_REMOVE_SECOND = (By.XPATH, "//*[@id = 'remove-sauce-labs-bike-light']")
    BTN_REMOVE_THIRD = (By.CSS_SELECTOR, "button#remove-sauce-labs-bolt-t-shirt")
    # BTN_REMOVE_THIRD = (By.XPATH, "//*[@id='remove-sauce-labs-bolt-t-shirt']")


class SideMenu:
    BTN_BURGER_MENU = (By.CSS_SELECTOR, "button#react-burger-menu-btn")
    # BTN_BURGER_MENU = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    LNK_LOGOUT = (By.CSS_SELECTOR, ".bm-item-list #logout_sidebar_link")
    # LNK_LOGOUT = (By.XPATH, "//*[contains(@class,'bm-item-list')]//*[@id='logout_sidebar_link']")
