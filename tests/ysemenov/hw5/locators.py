from selenium.webdriver.common.by import By


class LocatorsLoginPage:
    TXT_LOGIN = By.CSS_SELECTOR, "#user-name"
    TXT_PASSWORD = By.CSS_SELECTOR, "#password"
    BTN_SUBMIT = By.CSS_SELECTOR, "#login-button"


class LocatorsHeaderMenu:
    BTN_CART = By.CSS_SELECTOR, "#shopping_cart_container"
    CART_BADGE = By.CSS_SELECTOR, ".shopping_cart_badge"


class LocatorsInventoryPage:
    LST_INVENTORY = By.XPATH, ".//*[@class='inventory_item']"
    BTN_ADD_TO_CART = By.CSS_SELECTOR, ".pricebar .btn"
    LNK_PRODUCT_NAME = By.CSS_SELECTOR, "a[id^='item_']"


class LocatorsCartPage:
    LST_CART_ITEMS = By.XPATH, ".//*[@class='cart_item']"
    BTN_REMOVE_FROM_CART = By.CSS_SELECTOR, ".item_pricebar .btn"
    BTN_CONTINUE_SHOPPING = By.CSS_SELECTOR, "#continue-shopping"
    BTN_CHECKOUT = By.CSS_SELECTOR, "#checkout"


class LocatorsProductDetailsPage:
    BTN_ADD_TO_CART = By.CSS_SELECTOR, "#add-to-cart"
    BTN_REMOVE = By.CSS_SELECTOR, "#remove"
    BTN_BACK_TO_PRODUCTS = By.CSS_SELECTOR, "#back-to-products"


class LocatorsCheckoutPage:
    TXT_FIRST_NAME = By.CSS_SELECTOR, "#first-name"
    TXT_LAST_NAME = By.CSS_SELECTOR, "#last-name"
    TXT_POSTAL_CODE = By.CSS_SELECTOR, "#postal-code"
    BTN_CONTINUE = By.CSS_SELECTOR, "#continue"


class LocatorsOverviewPage:
    BTN_FINISH = By.CSS_SELECTOR, "#finish"


class LocatorsCompletePage:
    HEADER_COMPLETE = By.CSS_SELECTOR, "[data-test='complete-header']"
