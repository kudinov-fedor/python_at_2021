from selenium.webdriver.common.by import By


"""Login page locators"""
# before-> (By.ID, "user-name")
TXT_LOGIN_INPUT = (By.CSS_SELECTOR, "input.form_input.input_error#user-name")
# before-> (By.ID, "password")
TXT_PASSWORD_INPUT = (By.CSS_SELECTOR, "input.form_input.input_error#password[type='password']")
# before-> (By.ID, "login-button")
BTN_SUBMIT = (By.XPATH, "//input[@id='login-button']")


"""Landing page"""
# before-> (By.CSS_SELECTOR, ".inventory_list .inventory_item")
TABLE_PRODUCT_ITEMS = (By.XPATH, "//*[@class='inventory_list']/*[@class='inventory_item']")
# before-> (By.XPATH, ".//*[@class='pricebar']//button")
BTN_ADD_TO_CART = (By.CSS_SELECTOR, "div>button.btn_inventory.btn_small.btn.btn_primary")
# before-> (By.ID, "shopping_cart_container")
BTN_CART_LOCATE = (By.XPATH, "//div[@id='shopping_cart_container']")
# before-> (By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
TXT_CART_BADGE = (By.CSS_SELECTOR, "span.shopping_cart_badge")


"""Cart page"""
# before-> (By.CSS_SELECTOR, ".cart_list .cart_item")
TABLE_ITEMS_IN_CART = (By.XPATH, "//*[@class='cart_list']/*[@class='cart_item']")
# before-> (By.CSS_SELECTOR, ".btn_secondary.btn_small.cart_button")
BTN_REMOVE_FROM_CART = (By.XPATH, "//*[@class='cart_item']//button")
