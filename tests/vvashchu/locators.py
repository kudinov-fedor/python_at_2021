from selenium.webdriver.common.by import By


class Cart:
    # перевірка індикатора корзини
    # (By.ID, "shopping_cart_container")
    cart = (By.CSS_SELECTOR, "#shopping_cart_container")
    # (By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
    cart_badge = (By.CSS_SELECTOR, ".shopping_cart_badge")

    # перевірка кількості елементів в корзині
    # (By.CSS_SELECTOR, ".cart_list .cart_item")
    cart_items = (By.XPATH, ".//*[contains(@class,'cart_item')]")

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

    # видалення елементу
    # (By.CSS_SELECTOR, "button#remove-sauce-labs-backpack")
    remove_first_item_btn = (By.XPATH, "//*[@id='remove-sauce-labs-backpack']")


class LoginPage:
    # вхід в систему
    # (By.ID, "user-name")
    UserName = (By.XPATH, "//*[@id='user-name']")
    # (By.ID, "password")
    Password = ((By.XPATH, "//*[@id='password']"))
    # (By.ID, "login-button")
    Login_Btn = (By.XPATH, "//*[@id='login-button']")


class ProductPage:
    # додавання елементів
    # (By.CSS_SELECTOR, ".inventory_list .inventory_item")
    cart_items = (By.XPATH, "//div[contains(@class, 'inventory_list')]//div[contains(@class, 'inventory_item_description')]")
    # (By.XPATH, ".//*[@class='pricebar']//button")
    cart_items = (By.CSS_SELECTOR, ".pricebar button")
