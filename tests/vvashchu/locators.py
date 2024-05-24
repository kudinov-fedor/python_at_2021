from selenium.webdriver.common.by import By


class CartLocators:
    # перевірка кількості елементів в корзині
    # (By.CSS_SELECTOR, ".cart_list .cart_item")
    cart_items = (By.XPATH, "//*[contains(@class,'cart_list')]//*[@class='cart_item']")
    cart_item = (By.CSS_SELECTOR, ".cart_quantity")

    # перехід до оформлення замовлення
    # (By.ID, "checkout")
    checkout_btn = (By.CSS_SELECTOR, "#checkout")

    # заповнення форми замовлення
    # (By.ID, "first-name")
    FirstName = (By.XPATH, "//*[@id='first-name']")
    # (By.ID, "last-name")
    LastName = (By.XPATH, "//*[@id='last-name']")
    # (By.ID, "postal-code")
    PostalCode = (By.XPATH, "//*[@id='postal-code']")
    # (By.ID, "continue")
    continue_btn = (By.XPATH, "//*[@id='continue']")

    # виконання замовлення
    # (By.ID, "finish")
    finish_btn = (By.XPATH, "//*[@id='finish']")

    # перевірка, що корзина пуста
    # (By.ID, "back-to-products")
    back_home_btn = (By.CSS_SELECTOR, '#back-to-products')

    # видалення елементу
    # (By.CSS_SELECTOR, "button#remove-sauce-labs-backpack")
    remove_first_item_btn = (By.XPATH, "//button[@id='remove-sauce-labs-backpack']")


class LoginPageLocators:
    # вхід в систему
    # (By.ID, "user-name")
    UserName = (By.XPATH, "//*[@id='user-name']")
    # (By.ID, "password")
    Password = (By.XPATH, "//*[@id='password']")
    # (By.ID, "login-button")
    LoginBtn = (By.XPATH, "//*[@id='login-button']")


class ProductPageLocators:
    # додавання елементів
    # (By.CSS_SELECTOR, ".inventory_list .inventory_item")
    product = \
        (By.XPATH, "//div[contains(@class, 'inventory_list')]"
                   "//div[contains(@class, 'inventory_item_description')]")
    # (By.XPATH, ".//*[@class='pricebar']//button")
    product_add_to_cart_btn = (By.CSS_SELECTOR, ".pricebar button")

    # перевірка індикатора корзини
    # (By.ID, "shopping_cart_container")
    cart = (By.CSS_SELECTOR, "#shopping_cart_container")
    # (By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
    cart_badge = (By.CSS_SELECTOR, ".shopping_cart_badge")
