from selenium.webdriver.common.by import By


class LoginPage:
    # txtLogin = (By.ID, "user-name")
    # txtPassword = (By.ID, "password")
    # btnSubmit = (By.ID, "login-button")
    txtLogin = (By.CSS_SELECTOR, "#user-name")
    txtPassword = (By.CSS_SELECTOR, "#password")
    btnSubmit = (By.CSS_SELECTOR, "#login-button")


class HeaderMenu:
    # btnCart = (By.ID, "shopping_cart_container")
    # cartBadge = (By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
    btnCart = (By.CSS_SELECTOR, "#shopping_cart_container")
    cartBadge = (By.CSS_SELECTOR, ".shopping_cart_badge")


class InventoryPage:
    # lstInventory = (By.CSS_SELECTOR, ".inventory_list .inventory_item")
    # btnAddToCart = (By.XPATH, ".//*[@class='pricebar']//button")
    # lnkProductName = (By.XPATH, ".//*[contains(@id, 'item_')]")
    lstInventory = (By.XPATH, ".//*[@class='inventory_item']")
    btnAddToCart = (By.CSS_SELECTOR, ".pricebar .btn")
    lnkProductName = (By.CSS_SELECTOR, "a[id^='item_']")


class CartPage:
    # lstCartItems = (By.CSS_SELECTOR, ".cart_list .cart_item")
    # btnRemoveFromCart = (By.XPATH, ".//*[contains(@id, 'remove')]")
    # btnContinueShopping = (By.ID, "continue-shopping")
    # btnCheckout = (By.ID, "checkout")
    lstCartItems = (By.XPATH, ".//*[@class='cart_item']")
    btnRemoveFromCart = (By.CSS_SELECTOR, ".item_pricebar .btn")
    btnContinueShopping = (By.CSS_SELECTOR, "#continue-shopping")
    btnCheckout = (By.CSS_SELECTOR, "#checkout")


class ProductDescriptionPage:
    # btnAddToCart = (By.XPATH, ".//*[@id='add-to-cart']")
    # btnRemove = (By.XPATH, ".//*[@id='remove']")
    # btnBackToProducts = (By.ID, "back-to-products")
    btnAddToCart = (By.CSS_SELECTOR, "#add-to-cart")
    btnRemove = (By.CSS_SELECTOR, "#remove")
    btnBackToProducts = (By.CSS_SELECTOR, "#back-to-products")


class CheckoutPage:
    # txtFirstName = (By.ID, "first-name")
    # txtLastName = (By.ID, "last-name")
    # txtPostalCode = (By.ID, "postal-code")
    # btnContinue = (By.ID, "continue")
    txtFirstName = (By.CSS_SELECTOR, "#first-name")
    txtLastName = (By.CSS_SELECTOR, "#last-name")
    txtPostalCode = (By.CSS_SELECTOR, "#postal-code")
    btnContinue = (By.CSS_SELECTOR, "#continue")


class OverviewPage:
    # btnFinish = (By.ID, "finish")
    btnFinish = (By.CSS_SELECTOR, "#finish")


class CompletePage:
    # headerComplete = (By.XPATH, "//*[@data-test='complete-header']")
    headerComplete = (By.CSS_SELECTOR, "[data-test='complete-header']")
