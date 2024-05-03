from selenium.webdriver.common.by import By


class LoginPageLocators:
    TXT_USER_NAME = (By.CSS_SELECTOR, "input[name='user-name']")  # prev => By.ID, "user-name"
    TXT_PASSWORD = (By.CSS_SELECTOR, "input[name='password']")  # prev => By.ID, "password"
    BTN_LOGIN = (By.CSS_SELECTOR, "input[name='login-button']")  # prev => By.ID, "login-button"


class ProductsPageLocators:
    # prev => By.ID, "react-burger-menu-btn"
    BTN_BURGER_MENU = (By.CSS_SELECTOR, "button#react-burger-menu-btn")
    # prev => By.CSS_SELECTOR, ".bm-menu a[id]"
    LINK_MENU_ITEM = (By.CSS_SELECTOR, "a.menu-item")
    # prev =>  By.CSS_SELECTOR, "select[data-test='product-sort-container']"
    SELECT_SORT_PRODUCT = (By.XPATH, "//select[@data-test='product-sort-container']")
    # prev => By.CSS_SELECTOR, ".inventory_list .inventory_item"
    DIV_PRODUCT_CARD = (By.XPATH, "//div[@data-test='inventory-item']")
    # prev =>  By.CSS_SELECTOR, "div[data-test='inventory-item-price']"
    DIV_PRODUCT_PRICE = (By.XPATH, "//div[@class='inventory_item_price']")
    # prev => By.XPATH, ".//*[@class='pricebar']//button"
    BTN_ADD_TO_CART = (By.CSS_SELECTOR, "button[id^='add-to-cart']")

    @classmethod
    def option_sort(cls, value):
        return By.CSS_SELECTOR, f"option[value='{value}']"


class ShoppingCartLocators:
    # prev => By.CLASS_NAME, "shopping_cart_badge"
    ICON_CART_BADGE = (By.CSS_SELECTOR, "span[data-test='shopping-cart-badge']")
    # prev => By.ID, "shopping_cart_container"
    DIV_CART_CONTAINER = (By.CSS_SELECTOR, "div[id='shopping_cart_container']")
    # prev => By.CSS_SELECTOR, ".cart_list .cart_item"
    DIV_CART_ITEM = (By.XPATH, "//div[@data-test='inventory-item']")
    # prev => By.ID, "checkout"
    BTN_CHECKOUT = (By.XPATH, "//button[@id='checkout']")


class CheckoutInfoLocators:
    IP_FIRST_NAME = (By.CSS_SELECTOR, "input[data-test='firstName']")  # By.ID, "first-name"
    IP_LAST_NAME = (By.CSS_SELECTOR, "input[data-test='lastName']")  # By.ID, "last-name"
    IP_POSTAL_CODE = (By.CSS_SELECTOR, "input[data-test='postalCode']")  # By.ID, "postal-code"
    BTN_CONTINUE = (By.CSS_SELECTOR, "input[data-test='continue']")  # By.ID, "continue"


class CheckoutOverviewLocators:
    BTN_FINISH = (By.CSS_SELECTOR, "button[data-test='finish']")  # By.ID, "finish"
    BTN_BACK_HOME = (By.CSS_SELECTOR, "button[data-test=back-to-products]")  # By.ID, "back-to-products"
