from selenium.webdriver.common.by import By


class LoginPageLocators:
    # (By.XPATH, "user-name")
    USER_NAME_FIELD = (By.XPATH, "//*[@id='user-name']")

    # (By.XPATH, "#password")
    USER_PASS_FIELD = (By.XPATH, "//*[@id='password']")

    # (By.XPATH, "input.submit-button.btn_action")
    SUBMIT_LOGIN_BUTTON = (By.XPATH, "//input[contains(@class, 'submit-button')][contains(@class, 'btn_action')]")


# //*[contains(@class, 'cart_item')]//*[contains(@class, 'btn')]
class CartLocators:
    # Works on any page except the login one

    # (By.XPATH, "shopping_cart_container")
    CART = (By.XPATH, "//*[@id='shopping_cart_container']")

    # (By.XPATH, ".shopping_cart_badge[data-test='shopping-cart-badge']")
    CART_BADGE_ELEMENT = (By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')][@data-test='shopping-cart-badge']")

    # Works only on the cart page

    # (By.XPATH, ".cart_item")
    CART_ITEMS = (By.XPATH, "//*[@class='cart_item']")
    # (By.XPATH, ".cart_item  .btn")
    CART_ITEMS_REMOVE_BUTTON = (By.XPATH, "//*[contains(@class, 'cart_item')]//*[contains(@class, 'btn')]")

    # (By.XPATH, "#checkout")
    CHECKOUT_BUTTON = (By.XPATH, "//*[@id='checkout']")
    # (By.XPATH, ".btn[data-test='continue-shopping']")
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//*[contains(@class, 'btn')][@data-test='continue-shopping']")


class InventoryItemsLocators:
    # Works only on landing page

    # (By.XPATH, ".inventory_list .inventory_item")
    INVENTORY_ITEMS = (By.XPATH, "//*[contains(@class, 'inventory_list')]/*[contains(@class,'inventory_item')]")

    # (By.XPATH, ".btn")
    BUTTON = (By.XPATH, ".//button")

    # (By.XPATH, ".inventory_item_name")
    INVENTORY_ITEM_NAME = (By.XPATH, ".//*[contains(@class, 'inventory_item_name')]")

    # Works only on the item page

    # (By.XPATH, ".btn[data-test='add-to-cart']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@data-test='add-to-cart']")
    # (By.XPATH, "#remove")
    REMOVE_BUTTON = (By.XPATH, "//*[@id='remove']")


class CheckoutPageLocators:
    # (By.XPATH, "#first-name")
    FIRST_NAME = (By.XPATH, "//*[@id='first-name']")
    # (By.XPATH, "#last-name")
    LAST_NAME = (By.XPATH, "//*[@id='last-name']")
    # (By.XPATH, "#postal-code")
    POSTAL_CODE = (By.XPATH, "//*[@id='postal-code']")
    # (By.XPATH, ".btn[data-test='continue']")
    CONTINUE_BUTTON = (By.XPATH, "//*[contains(@class,'btn')][@data-test='continue']")
    # (By.XPATH, ".btn[data-test='finish']")
    FINISH_BUTTON = (By.XPATH, "//*[contains(@class,'btn')][@data-test='finish']")


class MenuButtonsLocators:
    # (By.XPATH, "#react-burger-menu-btn")
    BURGER_BUTTON = (By.XPATH, "//*[@id='react-burger-menu-btn']")
    # (By.XPATH, "#logout_sidebar_link")
    LOGOUT_BUTTON = (By.XPATH, "//*[@id='logout_sidebar_link']")
