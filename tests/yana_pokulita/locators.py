from selenium.webdriver.common.by import By


class Cart:
    # check cart indicator

    # (By.ID, "shopping_cart_container")
    ShoppingCart = (By.CSS_SELECTOR, ".shopping_cart_container")
    # (By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
    ShoppingCartBadge = (By.CSS_SELECTOR, ".shopping_cart_badge")

    # check number of items in the cart

    # (By.CSS_SELECTOR, ".cart_list .cart_item")
    CartItems = (By.XPATH, ".//*[@class='cart_item']")
    # (By.ID, "checkout")
    CheckOutBtn = (By.CSS_SELECTOR, ".checkout_button[name='checkout']")

    # delete element from the cart

    # (By.CSS_SELECTOR, "button#remove-sauce-labs-backpack")
    Remove1stItemBtn = (By.XPATH, "//button[@id='remove-sauce-labs-backpack']")

    # fill the form

    # (By.ID, "first-name")
    FirstName = (By.CSS_SELECTOR, "#first-name")
    # (By.ID, "last-name")
    LastName = (By.CSS_SELECTOR, "#last-name")
    # (By.ID, "postal-code")
    PostalCode = (By.CSS_SELECTOR, "#postal-code")
    # (By.ID, "continue")
    btnContinue = (By.CSS_SELECTOR, "#continue")

    # order submission

    # (By.ID, "finish")
    # (By.CSS_SELECTOR, "#finish")
    FinishBtn = (By.XPATH, "//button[@id= 'finish']")

    # go back to products

    # (By.ID, "back-to-products")
    BackHomeBtn = (By.CSS_SELECTOR, '#back-to-products')


class LoginPage:
    # loging to the system

    # (By.ID, "user-name")
    UserName = (By.NAME, "user-name")
    # (By.ID, "password")
    Password = (By.NAME, "password")
    # (By.ID, "login-button")
    LoginBtn = (By.NAME, "login-button")


class ProductPage:
    # adding elements

    # (By.CSS_SELECTOR, ".inventory_list .inventory_item")
    Elements = (By.XPATH, "//div[contains(@class, 'inventory_list')]//div[contains(@class, 'inventory_item_description')]")
    # (By.XPATH, ".//*[@class='pricebar']//button")
    Element = (By.CSS_SELECTOR, ".pricebar button")
