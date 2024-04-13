from selenium.webdriver.common.by import By


def test_item_details(session):
    """
    Log in to the site
    Find first product
    Save the name of the first product
    Navigate to the product details page
    Check opened URL
    Compare product name from Product list page with Product details page
    """
    product_page = 'https://www.saucedemo.com/inventory-item.html?id=4'
    items = session.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
    items[0].find_element(By.XPATH, ".//*[@class='pricebar']//button").click()
    item_name = items[0].find_element(By.CSS_SELECTOR, ".inventory_item_label .inventory_item_name ").text
    items[0].find_element(By.CSS_SELECTOR, ".inventory_item_label .inventory_item_name ").click()
    item_page = session.find_element(By.CSS_SELECTOR, ".inventory_details .inventory_details_name").text
    assert item_name == item_page
    current_page = session.current_url
    assert current_page == product_page


def test_add_to_card(session):
    """
    Log in to the site
    Check the amount of products on the page
    Find first product
    Add this product to the cart
    Check the amount of added products to the card by amount on the badge
    """
    items = session.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
    assert len(items) == 6
    items[0].find_element(By.XPATH, ".//*[@class='pricebar']//button").click()
    cart = session.find_element(By.ID, "shopping_cart_container")
    cart_badge = cart.find_element(By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
    assert cart_badge.text == '1'


def test_add_all_cart(session):
    """
    Log in to the site
    Find all product
    Add all product to the cart
    Check the amount of added products to the cart by amount on the badge
    """
    items = session.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
    for i in range(6):
        items[i].find_element(By.XPATH, ".//*[@class='pricebar']//button").click()
    cart = session.find_element(By.ID, "shopping_cart_container")
    cart_badge = cart.find_element(By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
    assert cart_badge.text == '6'


def test_navigation_to_cart(session):
    """
    Log in to the site
    Find fist product
    Add it to the cart
    Open cart page
    Compare name of added product from the cart with the name of the product from the products page
    """
    item_name = 'Sauce Labs Backpack'
    items = session.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
    items[0].find_element(By.XPATH, ".//*[@class='pricebar']//button").click()
    item = items[0].find_element(By.CSS_SELECTOR, ".inventory_item_label .inventory_item_name ").text
    assert item == item_name
    cart = session.find_element(By.ID, "shopping_cart_container")
    cart.find_element(By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]").click()
    cart_item = session.find_element(By.CSS_SELECTOR, ".cart_item .inventory_item_name").text
    assert item == cart_item


def test_continue_shopping(session):
    """
    Log in to the site
    Find first product
    Add it to the cart
    Click on the Continue shopping button
    Check the navigation to the Product page
    """
    product_page = 'https://www.saucedemo.com/inventory.html'
    items = session.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
    items[0].find_element(By.XPATH, ".//*[@class='pricebar']//button").click()
    cart = session.find_element(By.ID, "shopping_cart_container")
    cart.find_element(By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]").click()
    session.find_element(By.ID, "continue-shopping").click()
    current_page = session.current_url
    assert current_page == product_page


def test_navigate_checkout(session):
    """
    Log in to the site
    Add first product to the cart
    Click on the Checkout button
    Check that the Checkout step first is opened
    """
    checkout_step_one_page = 'https://www.saucedemo.com/checkout-step-one.html'
    items = session.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
    items[0].find_element(By.XPATH, ".//*[@class='pricebar']//button").click()
    cart = session.find_element(By.ID, "shopping_cart_container")
    cart.find_element(By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]").click()
    session.find_element(By.ID, "checkout").click()
    current_page = session.current_url
    assert current_page == checkout_step_one_page


def test_fill_order_form(session):
    """
    Log in to the site
    Add first product to the cart
    Click on the Checkout button
    Fill the checkout form
    Click on teh Continue button
    Compare added element with the element on the Checkout:Overview page
    Click on the Finish button
    Check that the Finish page is opened
    """
    finish_checkout = 'https://www.saucedemo.com/checkout-complete.html'
    items = session.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
    items[0].find_element(By.XPATH, ".//*[@class='pricebar']//button").click()
    item = items[0].find_element(By.CSS_SELECTOR, ".inventory_item_label .inventory_item_name ").text
    assert item == 'Sauce Labs Backpack'
    cart = session.find_element(By.ID, "shopping_cart_container")
    cart.find_element(By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]").click()
    session.find_element(By.ID, "checkout").click()
    session.find_element(By.ID, "first-name").send_keys("Adam")
    session.find_element(By.ID, "last-name").send_keys("Walter")
    session.find_element(By.ID, "postal-code").send_keys("90210")
    session.find_element(By.ID, "continue").click()
    checkout_item = session.find_element(By.CSS_SELECTOR, ".cart_item_label .inventory_item_name").text
    assert item == checkout_item
    session.find_element(By.ID, "finish").click()
    complete = session.find_element(By.CSS_SELECTOR, ".header_secondary_container .title").text
    assert complete == 'Checkout: Complete!'
    current_page = session.current_url
    assert current_page == finish_checkout
