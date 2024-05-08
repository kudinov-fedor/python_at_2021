from selenium.webdriver.common.by import By


class CartLocators:
    # check cart indicator

    ShoppingCart = (By.CSS_SELECTOR, "#shopping_cart_container")
    ShoppingCartBadge = (By.CSS_SELECTOR, ".shopping_cart_badge")

    # check number of items in the cart

    CartItems = (By.XPATH, ".//*[@class='cart_item']")
    CartItem = (By.CSS_SELECTOR, ".cart_quantity")
    CheckOutBtn = (By.CSS_SELECTOR, "#checkout")

    # delete element from the cart

    RemoveItemBtn = (By.CSS_SELECTOR, "button.cart_button")

    # fill the form

    FirstName = (By.CSS_SELECTOR, "#first-name")
    LastName = (By.CSS_SELECTOR, "#last-name")
    PostalCode = (By.CSS_SELECTOR, "#postal-code")
    btnContinue = (By.CSS_SELECTOR, "#continue")

    # order submission

    FinishBtn = (By.XPATH, "//button[@id= 'finish']")

    # go back to products

    BackHomeBtn = (By.CSS_SELECTOR, '#back-to-products')


class LoginPageLocators:
    # loging to the system

    UserName = (By.NAME, "user-name")
    Password = (By.NAME, "password")
    LoginBtn = (By.NAME, "login-button")


class ProductPageLocators:
    # adding elements

    Elements = (By.XPATH, "//div[contains(@class, 'inventory_list')]//div[contains(@class, 'inventory_item_description')]")
    Element = (By.CSS_SELECTOR, ".pricebar button")
