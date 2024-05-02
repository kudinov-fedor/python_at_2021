import pytest
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from locators import *


HOST = "https://www.saucedemo.com/"
user_name = "standard_user"
user_pass = "secret_sauce"

@pytest.fixture
def open_session():
    session = Chrome()
    session.get(HOST)

    yield session

    session.quit()


@pytest.fixture(autouse=True)
def login(open_session):
    open_session.find_element(*LoginPageLocators.USER_NAME_FIELD).send_keys(user_name)
    open_session.find_element(*LoginPageLocators.USER_PASS_FIELD).send_keys(user_pass)
    open_session.find_element(*LoginPageLocators.SUBMIT_LOGIN_BUTTON).click()


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
    elements = open_session.find_elements(*InventoryItemsLocators.INVENTORY_ITEMS)
    assert len(elements) == 6

    # Add an item to card from landing page
    elements[0].find_element(*InventoryItemsLocators.BUTTON).click()

    # Check Cart badge is updated
    cart = open_session.find_element(*CartLocators.CART)
    cart_badge = cart.find_element(*CartLocators.CART_BADGE_ELEMENT)
    assert cart_badge.text == '1'

    # Check Cart contains added item
    cart.click()
    assert len(open_session.find_elements(*CartLocators.CART_ITEMS)) == 1

    # Check Continue Shopping button
    open_session.find_element(*CartLocators.CONTINUE_SHOPPING_BUTTON).click()

    elements = open_session.find_elements(*InventoryItemsLocators.INVENTORY_ITEMS)

    # Open the item and add it to cart
    elements[5].find_element(*InventoryItemsLocators.INVENTORY_ITEM_NAME).click()
    assert "?id=" in str(open_session.current_url)

    open_session.find_element(*InventoryItemsLocators.ADD_TO_CART_BUTTON).click()

    # Check Cart and its badge are updated
    cart = open_session.find_element(*CartLocators.CART)
    cart_badge = cart.find_element(*CartLocators.CART_BADGE_ELEMENT)
    assert cart_badge.text == '2'

    cart.click()
    assert len(open_session.find_elements(*CartLocators.CART_ITEMS)) == 2

    # Checkout and confirm
    open_session.find_element(*CartLocators.CHECKOUT_BUTTON).click()

    open_session.find_element(*CheckoutPageLocators.FIRST_NAME).send_keys("1")
    open_session.find_element(*CheckoutPageLocators.LAST_NAME).send_keys("2")
    open_session.find_element(*CheckoutPageLocators.POSTAL_CODE).send_keys("3")
    open_session.find_element(*CheckoutPageLocators.CONTINUE_BUTTON).click()
    open_session.find_element(*CheckoutPageLocators.FINISH_BUTTON).click()


def test_delete_items(open_session):
    elements = open_session.find_elements(*InventoryItemsLocators.INVENTORY_ITEMS)
    cart = open_session.find_element(*CartLocators.CART)
    # Add three items to the cart
    elements[0].find_element(*InventoryItemsLocators.BUTTON).click()
    elements[1].find_element(*InventoryItemsLocators.BUTTON).click()
    elements[2].find_element(*InventoryItemsLocators.BUTTON).click()
    cart_badge = cart.find_element(*CartLocators.CART_BADGE_ELEMENT)
    assert cart_badge.text == '3'

    # Remove an item from the landing page
    elements[2].find_element(*InventoryItemsLocators.BUTTON).click()
    assert cart_badge.text == '2'

    # Remove an item from the Item page
    elements[1].find_element(*InventoryItemsLocators.INVENTORY_ITEM_NAME).click()
    open_session.find_element(*InventoryItemsLocators.REMOVE_BUTTON).click()

    cart = open_session.find_element(*CartLocators.CART)
    cart_badge = cart.find_element(*CartLocators.CART_BADGE_ELEMENT)
    assert cart_badge.text == '1'

    # Remove an item from the Cart page
    cart.click()

    cart_item = open_session.find_element(*CartLocators.CART_ITEMS)
    cart_item.find_element(*CartLocators.CART_ITEMS_REMOVE_BUTTON).click()
    assert len(open_session.find_elements(*CartLocators.CART_ITEMS)) == 0


def test_cart_is_empty(open_session):
    cart = open_session.find_element(*CartLocators.CART)
    # Ensure Cart badge is not displayed
    with pytest.raises(NoSuchElementException):
        open_session.find_element(*CartLocators.CART_BADGE_ELEMENT)
    cart.click()
    # Ensure cart is empty
    with pytest.raises(NoSuchElementException):
        open_session.find_element(*CartLocators.CART_ITEMS)


def test_logout(open_session):
    # Ensure user is logged in
    assert len(open_session.get_cookies()) != 0
    # Click on Menu Burger button
    open_session.find_element(*MenuButtonsLocators.BURGER_BUTTON).click()

    # TODO replace with wait
    time.sleep(1)

    # Click on Logout button
    open_session.find_element(*MenuButtonsLocators.LOGOUT_BUTTON).click()
    # Ensure user is logged out
    assert len(open_session.get_cookies()) == 0
