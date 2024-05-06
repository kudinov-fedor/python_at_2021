import pytest
import time
from selenium.webdriver import Chrome
from selenium.common import NoSuchElementException
from tests.innahoncharenko.homework_5.pages.locators import *

from config import Config
import pages

@pytest.fixture
def open_session():
    session = Chrome()
    session.get(Config.HOST)

    session.implicitly_wait(1)

    yield session

    session.quit()


@pytest.fixture
def landing_page(open_session):
    login_page = pages.LoginPage(open_session)
    return login_page \
        .set_user_name(Config.USER_NAME) \
        .set_password(Config.USER_PASS) \
        .submit()


def test_basic_flow(landing_page):
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

    products: list[pages.Product] = landing_page.get_items()

    assert len(products) == 6

    # Add an item to card from landing page
    products[0].add_item_to_cart()

    # Check Cart badge is updated
    assert landing_page.get_items_in_cart_number() == 1

    # Check Cart contains added item
    cart = landing_page.open_cart()
    assert cart.get_items_number() == 1

    # Check Continue Shopping button
    landing_page = cart.back_to_landing_page()

    # Open the item and add it to cart
    products: list[pages.Product] = landing_page.get_items()
    item_page = products[5].open_item()

    assert "?id=" in item_page.get_current_url()

    item_page.add_to_cart()
    # Check Cart and its badge are updated
    assert item_page.get_items_in_cart_number() == 2

    cart_page = item_page.open_cart()
    assert cart_page.get_items_number() == 2

    # Checkout and confirm
    checkout_page = cart_page.goto_checkout()
    finish_page = checkout_page.fill_form_and_continue(Config.USER_FIRST_NAME,
                                                       Config.USER_LAST_NAME,
                                                       Config.USER_POSTAL_CODE)
    finish_page.finish()


def test_delete_items(landing_page):
    # Add three items to the cart
    products = landing_page.get_items()
    products[0].add_item_to_cart()
    products[1].add_item_to_cart()
    products[2].add_item_to_cart()

    assert landing_page.get_items_in_cart_number() == 3
    # Remove an item from the landing page
    products[0].remove_item_from_cart()
    assert landing_page.get_items_in_cart_number() == 2
    item_page = products[1].open_item()

    # Remove an item from the Item page
    item_page.remove_from_cart()
    assert item_page.get_items_in_cart_number() == 1
    cart_page = item_page.open_cart()
    # Remove an item from the Cart page
    cart_page.remove_item(0)
    assert cart_page.get_items_number() == 0


def test_cart_is_empty(landing_page):
    # Ensure Cart badge is not displayed
    assert landing_page.get_items_in_cart_number() == 0

    cart = landing_page.open_cart()

    # Ensure cart is empty
    assert cart.get_items_number() == 0


def test_logout(open_session):
    login_page = pages.LoginPage(open_session)
    page = login_page \
        .set_user_name(Config.USER_NAME) \
        .set_password(Config.USER_PASS) \
        .submit()

    # Ensure user is logged in
    assert len(open_session.get_cookies()) != 0

    # Click on Menu Burger button
    page.click_element(MenuButtonsLocators.BURGER_BUTTON)
    # Click on Logout button
    page.click_element(MenuButtonsLocators.LOGOUT_BUTTON)

    # Ensure user is logged out
    assert len(open_session.get_cookies()) == 0
