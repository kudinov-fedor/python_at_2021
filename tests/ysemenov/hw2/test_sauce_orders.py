from selenium.webdriver import Chrome
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import pytest

HOST = "https://www.saucedemo.com"
LOGIN = "standard_user"
PASSWORD = "secret_sauce"


@pytest.fixture(scope="function")
def session():
    session = Chrome()
    yield session

    # tear down
    session.quit()


def test_order_product(session):
    """
    1. Log into the web store
    2. Add one product to cart
    3. Open cart
    4. Verify number of items added is 1
    5. Navigate to Checkout
    6. Fill in details and click Continue
    7. Finish the order
    8. Check that the order was successful
    """
    session.get(HOST)

    # 1. Log into the web store
    session.find_element(By.ID, "user-name").send_keys(LOGIN)
    session.find_element(By.ID, "password").send_keys(PASSWORD)
    session.find_element(By.ID, "login-button").click()

    # 2. Add one product to cart
    elements = session.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
    elements[0].find_element(By.XPATH, ".//*[@class='pricebar']//button").click()

    # 3. Open cart
    cart = session.find_element(By.ID, "shopping_cart_container")
    cart.click()

    # 4. Verify number of items added is 1
    items = session.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
    assert len(items) == 1

    # 5. Navigate to Checkout
    session.find_element(By.ID, "checkout").click()

    # 6. Fill in details and click Continue
    session.find_element(By.ID, "first-name").send_keys("Luke")
    session.find_element(By.ID, "last-name").send_keys("Skywalker")
    session.find_element(By.ID, "postal-code").send_keys("90210")
    session.find_element(By.ID, "continue").click()

    # 7. Finish the order
    session.find_element(By.ID, "finish").click()

    # 8. Check that the order was successful
    title_complete = session.find_element(By.XPATH, "//*[@data-test='complete-header']").text
    assert title_complete == "Thank you for your order!"


def test_add_remove_item(session):
    """
    1. Log into the web store
    2. Add one product to cart
    3. Verify cart label changed to 1
    4. Open cart
    5. Verify number of items in cart is 1
    6. Remove item from cart
    7. Verify number of items in cart is 0
    8. Go back to products page
    9. Verify cart label changed to none
    """
    session.get(HOST)

    # 1. Log into the web store
    session.find_element(By.ID, "user-name").send_keys(LOGIN)
    session.find_element(By.ID, "password").send_keys(PASSWORD)
    session.find_element(By.ID, "login-button").click()

    # 2. Add one product to cart
    elements = session.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
    elements[0].find_element(By.XPATH, ".//*[@class='pricebar']//button").click()

    # 3. Verify cart label changed to 1
    cart = session.find_element(By.ID, "shopping_cart_container")
    cart_badge = cart.find_element(By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
    assert cart_badge.text == '1'

    # 4. Open cart
    cart.click()

    # 5. Verify number of items in cart is 1
    items = session.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
    assert len(items) == 1

    # 6. Remove item from cart
    session.find_element(By.XPATH, ".//*[contains(@id, 'remove')]").click()

    # 7. Verify number of items in cart is 0
    items = session.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
    assert len(items) == 0

    # 8. Go back to products page
    session.find_element(By.ID, "continue-shopping").click()

    # 9. Verify cart label changed to none
    cart = session.find_element(By.ID, "shopping_cart_container")

    with pytest.raises(NoSuchElementException):
        cart.find_element(By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")


def test_add_to_cart_thru_product_page(session):
    """
    1. Log into the web store
    2. Open first product's page
    3. Click Add to cart
    4. Verify cart label is 1
    5. Remove item from cart
    6. Verify cart label is none
    7. Go back to products page
    """
    session.get(HOST)

    # 1. Log into the web store
    session.find_element(By.ID, "user-name").send_keys(LOGIN)
    session.find_element(By.ID, "password").send_keys(PASSWORD)
    session.find_element(By.ID, "login-button").click()

    # 2. Open first product's page
    elements = session.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
    elements[0].find_element(By.XPATH, ".//*[@id='item_4_title_link']").click()

    # 3. Open first product's page
    session.find_element(By.XPATH, ".//*[@id='add-to-cart']").click()

    # 4. Verify cart label is 1
    cart = session.find_element(By.ID, "shopping_cart_container")
    cart_badge = cart.find_element(By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
    assert cart_badge.text == '1'

    # 5. Remove item from cart
    session.find_element(By.XPATH, ".//*[@id='remove']").click()

    # 6. Verify cart items label is null
    cart = session.find_element(By.ID, "shopping_cart_container")

    with pytest.raises(NoSuchElementException):
        cart.find_element(By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")

    # 7. Go back to products page
    session.find_element(By.ID, "back-to-products").click()
