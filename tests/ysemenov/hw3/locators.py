from selenium.webdriver.common.by import By


class LoginPage:
    # txtLogin = By.ID, "user-name"
    # txtPassword = By.ID, "password"
    # btnSubmit = By.ID, "login-button"
    TXT_LOGIN = By.CSS_SELECTOR, "#user-name"
    TXT_PASSWORD = By.CSS_SELECTOR, "#password"
    BTN_SUBMIT = By.CSS_SELECTOR, "#login-button"


class HeaderMenu:
    # btnCart = By.ID, "shopping_cart_container"
    # cartBadge = By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]"
    BTN_CART = By.CSS_SELECTOR, "#shopping_cart_container"
    CART_BADGE = By.CSS_SELECTOR, ".shopping_cart_badge"


class InventoryPage:
    # lstInventory = By.CSS_SELECTOR, ".inventory_list .inventory_item"
    # btnAddToCart = By.XPATH, ".//*[@class='pricebar']//button"
    # lnkProductName = By.XPATH, ".//*[contains(@id, 'item_')]"
    LST_INVENTORY = By.XPATH, ".//*[@class='inventory_item']"
    BTN_ADD_TO_CART = By.CSS_SELECTOR, ".pricebar .btn"
    LNK_PRODUCT_NAME = By.CSS_SELECTOR, "a[id^='item_']"


class CartPage:
    # lstCartItems = By.CSS_SELECTOR, ".cart_list .cart_item"
    # btnRemoveFromCart = By.XPATH, ".//*[contains(@id, 'remove')]"
    # btnContinueShopping = By.ID, "continue-shopping"
    # btnCheckout = By.ID, "checkout"
    LST_CART_ITEMS = By.XPATH, ".//*[@class='cart_item']"
    BTN_REMOVE_FROM_CART = By.CSS_SELECTOR, ".item_pricebar .btn"
    BTN_CONTINUE_SHOPPING = By.CSS_SELECTOR, "#continue-shopping"
    BTN_CHECKOUT = By.CSS_SELECTOR, "#checkout"


class ProductDescriptionPage:
    # btnAddToCart = By.XPATH, ".//*[@id='add-to-cart']"
    # btnRemove = By.XPATH, ".//*[@id='remove']"
    # btnBackToProducts = By.ID, "back-to-products"
    BTN_ADD_TO_CART = By.CSS_SELECTOR, "#add-to-cart"
    BTN_REMOVE = By.CSS_SELECTOR, "#remove"
    BTN_BACK_TO_PRODUCTS = By.CSS_SELECTOR, "#back-to-products"


class CheckoutPage:
    # txtFirstName = By.ID, "first-name"
    # txtLastName = By.ID, "last-name"
    # txtPostalCode = By.ID, "postal-code"
    # btnContinue = By.ID, "continue"
    TXT_FIRST_NAME = By.CSS_SELECTOR, "#first-name"
    TXT_LAST_NAME = By.CSS_SELECTOR, "#last-name"
    TXT_POSTAL_CODE = By.CSS_SELECTOR, "#postal-code"
    BTN_CONTINUE = By.CSS_SELECTOR, "#continue"


class OverviewPage:
    # btnFinish = By.ID, "finish"
    BTN_FINISH = By.CSS_SELECTOR, "#finish"


class CompletePage:
    # headerComplete = By.XPATH, "//*[@data-test='complete-header']"
    HEADER_COMPLETE = By.CSS_SELECTOR, "[data-test='complete-header']"
