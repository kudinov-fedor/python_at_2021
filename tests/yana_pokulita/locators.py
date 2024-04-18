from selenium.webdriver.common.by import By


class Locators:
    # check cart indicator

    # (By.ID, "shopping_cart_container")
    shoppingCart = (By.CSS_SELECTOR, ".primary_header .shopping_cart_container")
    # (By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
    shoppingCartBadge = (By.CSS_SELECTOR, ".shopping_cart_link .shopping_cart_badge[data-test='shopping-cart-badge']")

    # check number of items in the cart

    # (By.CSS_SELECTOR, ".cart_list .cart_item")
    CartItems = (By.XPATH, ".//*[@class='cart_item']")
    # (By.ID, "checkout")
    CheckOutBtn = (By.CSS_SELECTOR, ".cart_footer .checkout_button[name='checkout'")

    # delete element from the cart

    # (By.CSS_SELECTOR, "button#remove-sauce-labs-backpack")
    Remove1stItemBtn = (By.XPATH, "//*[@id='remove-sauce-labs-backpack']")

    # fill the form

    # (By.ID, "first-name")
    FirstName = (By.CSS_SELECTOR, ".form_group .form_input[placeholder='First Name'")
    # (By.ID, "last-name")
    LastName = (By.CSS_SELECTOR, ".form_group .form_input[placeholder='Last Name'")
    # (By.ID, "postal-code")
    PostalCode = (By.CSS_SELECTOR, ".form_group .form_input[placeholder='Zip/Postal Code'")
    # (By.ID, "continue")
    btnContinue = (By.CSS_SELECTOR, ".checkout_buttons .submit-button[name='continue'")

    # order submission

    # (By.ID, "finish")
    FinishBtn = (By.CSS_SELECTOR, ".cart_footer .cart_button[data-test='finish'")

    # go back to products

    # (By.ID, "back-to-products")
    BackHomeBtn = (By.CSS_SELECTOR, '#back-to-products')


class ForConfTest:
    # loging to the system

    # (By.ID, "user-name")
    UserName = (By.NAME, "user-name")
    # (By.ID, "password")
    Password = (By.NAME, "password")
    # (By.ID, "login-button")
    LoginBtn = (By.NAME, "login-button")

    # adding elements

    # (By.CSS_SELECTOR, ".inventory_list .inventory_item")
    Elements = (By.XPATH, "//*[@class='inventory_item_description']//div[2]")
    # (By.XPATH, ".//*[@class='pricebar']//button")
    Element1 = (By.CSS_SELECTOR, ".pricebar .btn_inventory")
    # (By.XPATH, ".//*[@class='pricebar']//button")
    Element3 = (By.CSS_SELECTOR, ".pricebar .btn_inventory")
