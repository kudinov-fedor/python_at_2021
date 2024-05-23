from tests.ysemenov.hw5 import pages
from tests.ysemenov.hw5.conftest import LOGIN, PASSWORD, FIRSTNAME, LASTNAME, POSTALCODE, MESSAGE_SUCCESS


def test_order_product(session):
    """
    1. Log into the web store
    2. Add one product to cart
    3. Open cart
    4. Verify number of items in cart is 1
    5. Click Checkout to navigate to Checkout page
    6. Fill in details and click Continue
    7. Finish the order
    8. Check that the order was successful
    """

    # 1. Log into the web store
    login_page = pages.LoginPage(session)
    login_page.open()
    login_page.log_in(LOGIN, PASSWORD)

    # 2. Add one product to cart in the Inventory page
    inventory_page = pages.InventoryPage(session)
    inventory_page.add_product_to_cart(inventory_page.get_products()[0])  # 0 is the index of the first product

    # 3. Open cart
    inventory_page.click_cart_button()

    # 4. Verify number of items in cart is 1
    cart_page = pages.CartPage(session)
    assert len(cart_page.get_items_in_cart()) == 1, "Number of items in cart doesn't match expected value"

    # 5. Click Checkout to navigate to Checkout page
    cart_page.click_checkout()

    # 6. Fill in details and click Continue
    checkout_page = pages.CheckoutPage(session)
    checkout_page.submit_checkout_details(FIRSTNAME, LASTNAME, POSTALCODE)

    # 7. Finish the order
    overview_page = pages.OverviewPage(session)
    overview_page.finish_order()

    # 8. Check that the order was successful
    order_status_page = pages.OrderStatusPage(session)
    assert order_status_page.get_order_msg() == MESSAGE_SUCCESS, "Message doesn't match expected value"


def test_add_remove_item(session):
    """
    1. Log into the web store
    2. Add one product to cart in the Inventory page
    3. Verify cart items count label changed to 1
    4. Open cart
    5. Verify number of items in cart page is 1
    6. Remove item from cart
    7. Verify number of items in cart page is 0
    8. Go back to Products page
    9. Verify cart items count label changed to none
    """

    # 1. Log into the web store
    login_page = pages.LoginPage(session)
    login_page.open()
    login_page.log_in(LOGIN, PASSWORD)

    # 2. Add one product to cart in the Inventory page
    inventory_page = pages.InventoryPage(session)
    inventory_page.add_product_to_cart(inventory_page.get_products()[0])  # 0 is the index of the first product

    # 3. Verify cart items count label changed to 1
    cart_badge_number = inventory_page.get_cart_badge_number()
    assert cart_badge_number == 1, "Cart badge number doesn't match expected value"

    # 4. Open cart
    inventory_page.click_cart_button()

    # 5. Verify number of items in cart page is 1
    cart_page = pages.CartPage(session)
    assert len(cart_page.get_items_in_cart()) == 1, "Number of items in cart doesn't match expected value"

    # 6. Remove item from cart
    cart_page.remove_from_cart(cart_page.get_items_in_cart()[0])  # 0 is the index of the first product here

    # 7. Verify number of items in cart page is 0
    cart_page = pages.CartPage(session)
    assert len(cart_page.get_items_in_cart()) == 0, "Number of items in cart doesn't match expected value"

    # 8. Go back to Products page
    cart_page.click_continue_shopping()

    # 9. Verify cart items count label changed to none
    cart_badge_number = inventory_page.get_cart_badge_number()
    assert cart_badge_number == 0, "Cart badge number is not empty"


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

    # 1. Log into the web store
    login_page = pages.LoginPage(session)
    login_page.open()
    login_page.log_in(LOGIN, PASSWORD)

    # 2. Open first product's page
    inventory_page = pages.InventoryPage(session)
    inventory_page.open_product_page(inventory_page.get_products()[0])  # 0 is the index of the first product here

    # 3. Click Add to cart
    product_details_page = pages.ProductDetailsPage(session)
    product_details_page.add_to_cart()

    # 4. Verify cart label is 1
    cart_badge_number = product_details_page.get_cart_badge_number()
    assert cart_badge_number == 1, "Cart badge number doesn't match expected value"

    # 5. Remove item from cart
    product_details_page.remove_from_cart()

    # 6. Verify cart label is none
    cart_badge_number = product_details_page.get_cart_badge_number()
    assert cart_badge_number == 0, "Cart badge number is not empty"

    # 7. Go back to products page
    product_details_page.back_to_products()
