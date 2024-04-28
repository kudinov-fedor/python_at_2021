import pytest
from selenium.common import NoSuchElementException
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
    cart.cart_elements()
    cart_indicator = page.CartPage(session)
    cart_indicator.cart_badge()
    assert cart_indicator.cart_badge().text == '2'

    # go to cart
    cart.go_to_cart()

    # check nuber of items in the cart
    elements_in_cart = page.CartPage(session)
    elements_in_cart.get_cart_items()
    assert len(elements_in_cart.get_cart_items()) == 2

    # go to checkout
    cart.go_to_checkout()

    # fill the order form
    checkout_page = page.CheckoutInformationPage(session)
    checkout_page.fill_order_form('Jonh', 'Adams', '001011')

    # order submission
    checkout_page = page.CheckoutOverviewPage(session)
    checkout_page.finish_order()

    # check that cart is empty
    checkout_page = page.CheckoutCompletePage(session)
    checkout_page.back_to_products()
    cart = page.CartPage(session)

    with pytest.raises(NoSuchElementException):
        cart.cart_badge()


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
    cart.cart_elements()
    cart_indicator = page.CartPage(session)
    cart_indicator.cart_badge()
    assert cart_indicator.cart_badge().text == '2'

    # go to cart
    cart.go_to_cart()

    # check nuber of items in the cart
    elements_in_cart = page.CartPage(session)
    elements_in_cart.get_cart_items()
    assert len(elements_in_cart.get_cart_items()) == 2

    # delete element
    elements_in_cart.remove_cart_item(0)

    # check nuber of items in the cart
    elements_in_cart.get_cart_items()
    assert len(elements_in_cart.get_cart_items()) == 1


def test_cart_is_empty_after_login(session):
    """
    login
    go to cart
    check number cart is empty
    """

    # go to cart
    cart = page.CartPage(session)
    cart.go_to_cart()

    # check nuber of items in the cart
    elements_in_cart = page.CartPage(session)
    elements_in_cart.get_cart_items()
    assert len(elements_in_cart.get_cart_items()) == 0


def test_checkout_disabled_if_cart_empty(session):
    """
    login
    go to cart
    check checkout is disabled
    """
    # go to cart
    cart = page.CartPage(session)
    cart.go_to_cart()

    cart.checkout_btn_status()
    assert cart.checkout_btn_status() is False
