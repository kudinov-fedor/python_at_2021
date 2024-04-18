import pytest
from selenium.common import NoSuchElementException
from tests.yana_pokulita.locators import Locators


@pytest.mark.usefixtures("cart_with_2_items")
def test_basic_flow(session):
    """
    check number of products on the page
    add 2 products to the cart
    check cart indicator
    go to cart
    check number of products in cart
    go to checkout
    fill the form
    check that cart is empty after order submission
    """

    # check indicator of cart
    cart = session.find_element(*Locators.shoppingCart)
    cart_badge = cart.find_element(*Locators.shoppingCartBadge)
    assert cart_badge.text == '2'

    # go to cart
    cart.click()

    # check nuber of items in the cart
    items = session.find_elements(*Locators.CartItems)
    assert len(items) == 2

    # go to checkout
    session.find_element(*Locators.CheckOutBtn).click()

    # fill the order form
    session.find_element(*Locators.FirstName).send_keys("Jonh")
    session.find_element(*Locators.LastName).send_keys("Adams")
    session.find_element(*Locators.PostalCode).send_keys("001011")
    session.find_element(*Locators.btnContinue).click()

    # order submission
    session.find_element(*Locators.FinishBtn).click()

    # check that cart is empty
    session.find_element(*Locators.BackHomeBtn).click()
    cart = session.find_element(*Locators.shoppingCart)

    with pytest.raises(NoSuchElementException):
        cart.find_element(*Locators.shoppingCartBadge)


@pytest.mark.usefixtures("cart_with_2_items")
def test_product_can_be_removed_flow(session):
    """
    check number of products on the page
    add 2 products to the cart
    go to cart
    check number of products in cart
    delete one product
    check number of products in cart
    """

    # check indicator of cart
    cart = session.find_element(*Locators.shoppingCart)
    cart_badge = cart.find_element(*Locators.shoppingCartBadge)
    assert cart_badge.text == '2'

    # go to cart
    cart.click()

    # check nuber of items in the cart
    items = session.find_elements(*Locators.CartItems)
    assert len(items) == 2

    # delete element
    items[0].find_element(*Locators.Remove1stItemBtn).click()

    # check nuber of items in the cart
    items = session.find_elements(*Locators.CartItems)
    assert len(items) == 1


def test_cart_is_empty_after_login(session):
    """
    login
    go to cart
    check number cart is empty
    """

    # go to cart
    cart = session.find_element(*Locators.shoppingCart)
    cart.click()

    # check nuber of items in the cart
    items = session.find_elements(*Locators.CartItems)
    assert len(items) == 0


def test_checkout_disabled_if_cart_empty(session):
    """
    login
    go to cart
    check checkout is disabled
    """
    # go to cart
    cart = session.find_element(*Locators.shoppingCart)
    cart.click()

    checkout_button = session.find_element(*Locators.CheckOutBtn).is_enabled()
    assert checkout_button is False
