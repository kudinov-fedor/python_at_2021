import pytest
from tests.mariana_petrushanska.test_selenium_hw5 import constants
from tests.mariana_petrushanska.test_selenium_hw5 import CartPage, InformationPage, OverviewPage, SuccessPage, ProductsPage


def test_no_order_with_0_items_possible(session):
    """
    Check that cart is empty when user logs in:
    1. Log in (covered with "login" fixture).
    2. Click on the cart item.
    3. Check number of items in the cart.
    4. Check that 'Checkout' button is disabled.
    """

    # 2. Click on the cart item.
    product_page = ProductsPage(session)
    product_page.go_to_cart()

    # 3. Check number of items in the cart.
    cart_page = CartPage(session)
    assert len(cart_page.get_items_in_cart()) == 0

    # 4. Check that 'Checkout' button is disabled.
    assert cart_page.check_checkout_btn() is False


@pytest.mark.usefixtures("three_items_in_the_cart")
def test_complete_order_with_3_items(session):
    """
    1. Log in (covered with "login" fixture).
    2. Check number of items on the page (covered with "three_items_in_the_cart" fixture).
    3. Add 3 items (covered with "three_items_in_the_cart" fixture).
    4. Check number of items in the cart (number on the cart indicator).
    5. Go to cart.
    6. Check number of items in the cart.
    7. Click on 'Checkout' button.
    8. Fill in user's information.
    9. Click on 'Continue' button.
    10. Click on 'Finish' button.
    11. Click on 'Back Home' button on 'Success' page.
    12. Check that the cart is empty.
    """

    # 4. Check number of items in the cart (number on the cart indicator).
    product_page = ProductsPage(session)
    assert product_page.get_cart_badge_number() == 3

    # 5. Go to cart.
    product_page.go_to_cart()

    # 6. Check number of items in the cart.
    cart_page = CartPage(session)
    assert len(cart_page.get_items_in_cart()) == 3

    # 7. Click on 'Checkout' button.
    cart_page.go_to_checkout_page()

    # 8. Fill in user's information.
    # 9. Click on 'Continue' button.
    information_page = InformationPage(session)
    overview_page = ((information_page
                     .fill_in_delivery_form(constants.FIRST_NAME, constants.LAST_NAME, constants.POSTAL_CODE))
                     .submit_form())

    # 10. Click on 'Finish' button on Overview page.
    overview_page.finish_order()

    # 11. Click on 'Back Home' button on 'Success' page.
    # 12. Check that the cart is empty.
    success_page = SuccessPage(session)
    success_page.go_to_homepage()


@pytest.mark.usefixtures("three_items_in_the_cart")
def test_items_removal(session):
    """
    1. Log in (covered with "login" fixture).
    2. Check number of items on the page (covered with "three_items_in_the_cart" fixture).
    3. Add 3 items (covered with "three_items_in_the_cart" fixture).
    4. Check number of items in the cart (number on the cart indicator).
    5. Go to cart.
    6. Check number of items in the cart.
    7. Remove 2nd item.
    8. Check number of items in the cart to make sure it is updated accordingly.
    """

    # 4. Check number of items in the cart (number on the cart indicator).
    product_page = ProductsPage(session)
    assert product_page.get_cart_badge_number() == 3

    # 5. Go to cart.
    product_page.go_to_cart()

    # 6. Check number of items in the cart.
    cart_page = CartPage(session)
    assert len(cart_page.get_items_in_cart()) == 3

    # 7. Remove 2nd item.
    items = cart_page.get_items_in_cart()
    cart_page.remove_item(items[1])

    # 8. Check number of items in the cart to make sure it is updated accordingly.
    assert len(cart_page.get_items_in_cart()) == 2


@pytest.mark.usefixtures("three_items_in_the_cart")
def test_item_total(session):
    """
    1. Log in (covered with "login" fixture).
    2. Check number of items on the page (covered with "three_items_in_the_cart" fixture).
    3. Add 3 items (covered with "three_items_in_the_cart" fixture).
    4. Go to cart.
    5. Click on 'Checkout' button.
    6. Fill in user's information.
    7. Click on 'Continue' button.
    8. Calculate the sum of all items' prices.
    9. Check that calculated sum = 'Item total' value on the page.
    """

    # 4. Go to cart.
    product_page = ProductsPage(session)
    product_page.go_to_cart()

    # 5. Click on 'Checkout' button.
    cart_page = CartPage(session)
    cart_page.go_to_checkout_page()

    # 6. Fill in user's information.
    # 7. Click on 'Continue' button.
    information_page = InformationPage(session)
    overview_page = ((information_page
                      .fill_in_delivery_form(constants.FIRST_NAME, constants.LAST_NAME, constants.POSTAL_CODE))
                     .submit_form())

    # 8. Calculate the sum of all items' prices.
    # 9. Check that calculated sum = 'Item total' value on the page.
    overview_page = OverviewPage(session)
    items = overview_page.get_items()
    calculated_sum = sum([overview_page.item_price(item) for item in items])
    assert calculated_sum == overview_page.total()
