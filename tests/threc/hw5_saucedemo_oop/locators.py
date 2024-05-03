from selenium.webdriver.common.by import By


class LocSignupPage:
    # login = (By.ID, "user-name")
    login = (By.CSS_SELECTOR, ".login-box .input_error[placeholder='Username']")

    # password = (By.ID, "password")
    password = (By.CSS_SELECTOR, ".login-box .input_error[placeholder='Password']")

    # btnLogin = (By.ID, "login-button")
    btnLogin = (By.CSS_SELECTOR, ".submit-button.btn_action[name='login-button']")


class LocProductsPage:
    listProducts = (By.CSS_SELECTOR, ".inventory_list .inventory_item")
    btnAddToCart = (By.CSS_SELECTOR, ".pricebar button")
    productTitle = (By.CSS_SELECTOR, ".inventory_item_name")
    productDetailsPage = (By.CSS_SELECTOR, ".inventory_details_name")


class LocCartPage:
    cartBadge = (By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
    cartLink = (By.CSS_SELECTOR, ".shopping_cart_container .shopping_cart_link")
    cartProductName = (By.XPATH, "//*[@id='item_4_title_link']/div")


class LocCheckoutPage:
    # btnCheckout = (By.ID, "checkout")
    btnCheckout = (By.CSS_SELECTOR, ".cart_footer .checkout_button[name='checkout'")
    checkoutItem = (By.CSS_SELECTOR, ".cart_item_label .inventory_item_name")
    # btnContinueShopping = (By.ID, "continue-shopping")
    btnContinueShopping = (By.CSS_SELECTOR, ".cart_footer .btn_medium[name='continue-shopping'")


class LocFillForm:
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

    finishOrderTitle = (By.CSS_SELECTOR, ".header_secondary_container .title")
    # finishOrderTitle = (By.XPATH, "//*[@id='header_container']/div[2]/span")
