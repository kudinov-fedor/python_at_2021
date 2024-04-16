from selenium.webdriver.common.by import By


class LoginPage:
    # login = (By.ID, "user-name")
    login = (By.CSS_SELECTOR, ".login-box .input_error[placeholder='Username']")

    # password = (By.ID, "password")
    password = (By.CSS_SELECTOR, ".login-box .input_error[placeholder='Password']")

    # btnLogin = (By.ID, "login-button")
    btnLogin = (By.CSS_SELECTOR, ".submit-button.btn_action[name='login-button']")


class ProductsPage:
    # listProducts = (By.CSS_SELECTOR, ".inventory_list .inventory_item")
    listProducts = (By.XPATH, "//*[@class='inventory_item_description']//div[2]")

    # btnAddToCard = (By.XPATH, ".//*[@class='pricebar']//button")
    btnAddToCart = (By.CSS_SELECTOR, ".pricebar .btn_inventory ")

    # btnProductDetails = (By.CSS_SELECTOR, ".inventory_item_label .inventory_item_name")
    btnProductDetails = (By.XPATH, "//*[@id='item_4_title_link']/div")

    # productDetailsPage = (By.CSS_SELECTOR, ".inventory_details .inventory_details_name")
    productDetailsPage = (By.XPATH, "//*[@id='inventory_item_container']/div/div/div[2]/div[1]")


class CartPage:
    # shoppingCart = (By.ID, "shopping_cart_container")
    shoppingCart = (By.CSS_SELECTOR, ".primary_header .shopping_cart_container")

    # cartBadge = (By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
    cartBadge = (By.CSS_SELECTOR, ".shopping_cart_link .shopping_cart_badge[data-test='shopping-cart-badge']")

    # cartProductName = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
    cartProductName = (By.XPATH, "//*[@id='item_4_title_link']/div")


class CheckoutPage:
    # btnCheckout = (By.ID, "checkout")
    btnCheckout = (By.CSS_SELECTOR, ".cart_footer .checkout_button[name='checkout'")

    # checkoutItem = (By.CSS_SELECTOR, ".cart_item_label .inventory_item_name")
    checkoutItem = (By.XPATH, "//*[@id='item_4_title_link']/div")

    # btnContinueShopping = (By.ID, "continue-shopping")
    btnContinueShopping = (By.CSS_SELECTOR, ".cart_footer .btn_medium[name='continue-shopping'")


class FillForm:
    # firstName = (By.ID, "first-name")
    firstName = (By.CSS_SELECTOR, ".form_group .form_input[placeholder='First Name'")

    # lastName = (By.ID, "last-name")
    lastName = (By.CSS_SELECTOR, ".form_group .form_input[placeholder='Last Name'")

    # zipCode = (By.ID, "postal-code")
    zipCode = (By.CSS_SELECTOR, ".form_group .form_input[placeholder='Zip/Postal Code'")

    # btnContinue = (By.ID, "continue")
    btnContinue = (By.CSS_SELECTOR, ".checkout_buttons .submit-button[name='continue'")

    # btnFinish = (By.ID, "finish")
    btnFinish = (By.CSS_SELECTOR, ".cart_footer .cart_button[data-test='finish'")

    # finishOrderTitle = (By.CSS_SELECTOR, ".header_secondary_container .title")
    finishOrderTitle = (By.XPATH, "//*[@id='header_container']/div[2]/span")
