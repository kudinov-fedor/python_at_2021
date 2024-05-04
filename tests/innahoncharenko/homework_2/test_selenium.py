import pytest
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException


HOST = "https://www.saucedemo.com/"
user_name = "standard_user"
user_pass = "secret_sauce"


@pytest.fixture
def open_session():
    session = Chrome()

    session.implicitly_wait(1)

    session.get(HOST)

    yield session

    session.quit()


@pytest.fixture(autouse=True)
def login(open_session):
    open_session.find_element(By.ID, "user-name").send_keys(user_name)
    open_session.find_element(By.CSS_SELECTOR, "#password").send_keys(user_pass)
    open_session.find_element(By.CSS_SELECTOR, "input.submit-button.btn_action").click()


def test_basic_flow(open_session):
    """
    Check number of items on page
    add 1 item to cart from landing page
    check cart badge is updated
    check element is added to cart
    check Continue Shopping button
    open another item
    add to card
    check cart badge is updated
    open cart and check it has 2 items
    checkout and confirm
    """

    # Check the number of items on the landing page
    elements = open_session.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
    assert len(elements) == 6

    # Add an item to card from landing page
    elements[0].find_element(By.CSS_SELECTOR, ".btn").click()

    # Check Cart badge is updated
    cart = open_session.find_element(By.ID, "shopping_cart_container")
    cart_badge = cart.find_element(By.CSS_SELECTOR, ".shopping_cart_badge[data-test='shopping-cart-badge']")
    assert cart_badge.text == '1'

    # Check Cart contains added item
    cart.click()
    assert len(open_session.find_elements(By.CSS_SELECTOR, ".cart_item")) == 1

    # Check Continue Shopping button
    open_session.find_element(By.CSS_SELECTOR, ".btn[data-test='continue-shopping']").click()

    elements = open_session.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")

    # Open the item and add it to cart
    elements[5].find_element(By.CSS_SELECTOR, ".inventory_item_name").click()
    assert "?id=" in str(open_session.current_url)
    open_session.find_element(By.CSS_SELECTOR, ".btn[data-test='add-to-cart']").click()

    # Check Cart and its badge are updated
    cart = open_session.find_element(By.ID, "shopping_cart_container")
    cart_badge = cart.find_element(By.CSS_SELECTOR, ".shopping_cart_badge[data-test='shopping-cart-badge']")
    assert cart_badge.text == '2'
    cart.click()
    assert len(open_session.find_elements(By.CSS_SELECTOR, ".cart_item")) == 2

    # Checkout and confirm
    open_session.find_element(By.CSS_SELECTOR, "#checkout").click()
    open_session.find_element(By.CSS_SELECTOR, "#first-name").send_keys("1")
    open_session.find_element(By.CSS_SELECTOR, "#last-name").send_keys("2")
    open_session.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("3")
    open_session.find_element(By.CSS_SELECTOR, ".btn[data-test='continue']").click()
    open_session.find_element(By.CSS_SELECTOR, ".btn[data-test='finish']").click()


def test_delete_items(open_session):
    elements = open_session.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
    cart = open_session.find_element(By.ID, "shopping_cart_container")

    # Add three items to the cart
    elements[0].find_element(By.CSS_SELECTOR, ".btn").click()
    elements[1].find_element(By.CSS_SELECTOR, ".btn").click()
    elements[2].find_element(By.CSS_SELECTOR, ".btn").click()
    cart_badge = cart.find_element(By.CSS_SELECTOR, ".shopping_cart_badge[data-test='shopping-cart-badge']")
    assert cart_badge.text == '3'

    # Remove an item from the landing page
    elements[2].find_element(By.CSS_SELECTOR, ".btn").click()
    assert cart_badge.text == '2'

    # Remove an item from the Item page
    elements[1].find_element(By.CSS_SELECTOR, ".inventory_item_name").click()

    open_session.find_element(By.CSS_SELECTOR, "#remove").click()
    cart = open_session.find_element(By.ID, "shopping_cart_container")
    cart_badge = cart.find_element(By.CSS_SELECTOR, ".shopping_cart_badge[data-test='shopping-cart-badge']")
    assert cart_badge.text == '1'

    # Remove an item from the Cart page
    cart.click()

    cart_item = open_session.find_element(By.CSS_SELECTOR, ".cart_item")
    cart_item.find_element(By.CSS_SELECTOR, ".btn").click()
    assert len(open_session.find_elements(By.CSS_SELECTOR, ".cart_item")) == 0


def test_cart_is_empty(open_session):
    cart = open_session.find_element(By.ID, "shopping_cart_container")

    # Ensure Cart badge is not displayed
    with pytest.raises(NoSuchElementException):
        open_session.find_element(By.CSS_SELECTOR, ".shopping_cart_badge[data-test='shopping-cart-badge']")
    cart.click()

    # Ensure cart is empty
    with pytest.raises(NoSuchElementException):
        open_session.find_element(By.CSS_SELECTOR, ".cart_item")


def test_logout(open_session):
    # Ensure user is logged in
    assert len(open_session.get_cookies()) != 0
    # Click on Menu Burger button
    open_session.find_element(By.CSS_SELECTOR, "#react-burger-menu-btn").click()
    # Click on Logout button
    open_session.find_element(By.CSS_SELECTOR, "#logout_sidebar_link").click()
    # Ensure user is logged out
    assert len(open_session.get_cookies()) == 0
