from selenium.webdriver.common.by import By


class LogIn:

    # By.ID, "user-name"
    USER_NAME = (By.CSS_SELECTOR, "#user-name")

    # (By.ID, "password")
    PASSWORD = (By.CSS_SELECTOR, "#password")

    # (By.ID, "login-button")
    BTN_LOGIN = (By.CSS_SELECTOR, "#login-button")


class AddItems:

    # (By.CSS_SELECTOR, ".inventory_list .inventory_item")
    INVENTORY_ITEMS = (By.XPATH, "//*[contains(@class,'inventory_list')]/*[contains(@class,'inventory_item')]")

    # (By.XPATH, ".//*[@class='pricebar']//button")
    BTN_ADD_TO_CART = (By.CSS_SELECTOR, ".pricebar button")


class ShoppingCart:
    # verify shop cart badge

    # By.ID, "shopping_cart_container")
    CART_CONTAINER = (By.CSS_SELECTOR, ".shopping_cart_container")
    # (By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")

    # verify the number in cart

    # (By.CSS_SELECTOR, ".cart_list .cart_item")
    CART_LIST = (By.XPATH, ".//*[@class='cart_item']")
    # (By.ID, "checkout")
    BTN_CHECKOUT = (By.CSS_SELECTOR, "#checkout")

    # fill in the order form

    # (By.ID, "first-name")
    FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    # (By.ID, "last-name")
    LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    # (By.ID, "postal-code")
    POSTAL_CODE = (By.CSS_SELECTOR, "#postal-code")
    # (By.ID, "continue")
    BTN_CONTINUE = (By.CSS_SELECTOR, "#continue")

    # submitting order

    # (By.ID, "finish")
    BTN_FINISH = (By.CSS_SELECTOR, "#finish")

    # back to Product list

    # (By.ID, "back-to-products")
    BACK_TO_PRODUCT = (By.CSS_SELECTOR, "#back-to-products")

    # remove one product

    # (By.CSS_SELECTOR, "button#remove-sauce-labs-backpack")
    REMOVE_ITEM= (By.XPATH, "//button[@id='remove-sauce-labs-backpack']")
