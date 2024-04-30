import pytest
from tests.yana_pokulita.HW4_DemoQA import page


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

    cart = page.CartPage(session)
    assert cart.get_cart_badge() == 2

    # go to cart
    cart.go_to_cart_page()

    # check nuber of items in the cart
    assert len(cart.get_cart_items()) == 2

    # go to checkout
    cart.go_to_checkout_page()

    # fill the order form
    checkout_page = page.CheckoutInformationPage(session)
    checkout_page.fill_order_form('Jonh', 'Adams', '001011')

    # order submission
    checkout_page = page.CheckoutOverviewPage(session)
    checkout_page.finish_order()

    # check that cart is empty
    checkout_page = page.CheckoutCompletePage(session)
    checkout_page.back_to_products()
    assert cart.get_cart_badge() == 0


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
    cart = page.CartPage(session)
    assert cart.get_cart_badge() == 2

    # go to cart
    cart.go_to_cart_page()

    # check nuber of items in the cart
    assert len(cart.get_cart_items()) == 2

    # delete element
    cart.remove_cart_item(0)

    # check nuber of items in the cart
    assert len(cart.get_cart_items()) == 1


def test_cart_is_empty_after_login(session):
    """
    login
    go to cart
    check number cart is empty
    """

    # go to cart
    cart = page.CartPage(session)
    cart.go_to_cart_page()

    # check nuber of items in the cart
    assert len(cart.get_cart_items()) == 0


def test_checkout_disabled_if_cart_empty(session):
    """
    login
    go to cart
    check checkout is disabled
    """
    # go to cart
    cart = page.CartPage(session)
    cart.go_to_cart_page()

    assert cart.is_checkout_enabled() is False
