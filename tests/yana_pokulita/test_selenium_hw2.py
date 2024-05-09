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

    # check indicator of cart on the product page

    product_page = page.ProductsPage(session)
    assert product_page.get_cart_badge() == 2

    # go to cart page
    product_page.go_to_cart_page()

    # check nuber of items on the cart page
    cart_page = page.CartPage(session)
    products_in_cart = cart_page.get_cart_items()
    assert len(products_in_cart) == 2

    # go to checkout
    cart_page.go_to_checkout_page()

    # fill the order form
    checkout_info_page = page.CheckoutInformationPage(session)
    checkout_info_page.fill_order_form('Jonh', 'Adams', '001011')

    # order submission
    checkout_overview_page = page.CheckoutOverviewPage(session)
    checkout_overview_page.finish_order()

    # check that cart is empty
    checkout_complete_page = page.CheckoutCompletePage(session)
    checkout_complete_page.back_to_products()
    assert product_page.get_cart_badge() == 0


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

    # check indicator of cart on the product page
    product_page = page.ProductsPage(session)
    assert product_page.get_cart_badge() == 2

    # go to cart page
    product_page.go_to_cart_page()

    # check nuber of items in the cart page
    cart_page = page.CartPage(session)
    products_in_cart = cart_page.get_cart_items()
    assert len(products_in_cart) == 2

    # delete element from the cart
    products_in_cart[0].remove_cart_item()

    # check nuber of items on the cart page
    products_in_cart = cart_page.get_cart_items()
    assert len(products_in_cart) == 1


def test_cart_is_empty_after_login(session):
    """
    login
    go to cart
    check number cart is empty
    """

    # go to cart page from the product page
    product_page = page.ProductsPage(session)
    product_page.go_to_cart_page()

    # check number of items on the cart page
    cart_page = page.CartPage(session)
    products_in_cart = cart_page.get_cart_items()
    assert len(products_in_cart) == 0


def test_checkout_disabled_if_cart_empty(session):
    """
    login
    go to cart
    check checkout is disabled
    """
    # go to cart page from the product page
    product_page = page.ProductsPage(session)
    product_page.go_to_cart_page()

    # check checkout button on the cart page
    cart_page = page.CartPage(session)
    assert cart_page.is_checkout_enabled() is False
