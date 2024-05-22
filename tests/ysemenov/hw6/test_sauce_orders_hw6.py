from selenium.webdriver.chrome.webdriver import WebDriver
from tests.ysemenov.hw6.pages import InventoryPage
from tests.ysemenov.hw6.constants import FIRSTNAME, LASTNAME, POSTALCODE, MESSAGE_SUCCESS


def test_order_product(session: WebDriver, landing_page: InventoryPage):
    """
    1. Log into the web store -- skipped, as it's done in the setup fixture
    2. Add one product to cart
    3. Open cart
    4. Verify number of items in cart is 1
    5. Click Checkout to navigate to Checkout page
    6. Fill in details and click Continue
    7. Finish the order
    8. Check that the order was successful
    """

    # 2. Add one product to cart in the Inventory page
    products = landing_page.products
    products[0].add_to_cart()  # 0 is the index of the first product

    # 3. Open cart
    cart_page = landing_page.click_cart_button()

    # 4. Verify number of items in cart is 1
    assert len(cart_page.items_in_cart) == 1, "Number of items in cart doesn't match expected value"

    # 5. Click Checkout to navigate to Checkout page
    checkout_page = cart_page.click_checkout()

    # 6. Fill in details and click Continue
    overview_page = checkout_page.submit_checkout_details(FIRSTNAME, LASTNAME, POSTALCODE)

    # 7. Finish the order
    order_status_page = overview_page.finish_order()

    # 8. Check that the order was successful
    assert order_status_page.order_msg == MESSAGE_SUCCESS, "Message doesn't match expected value"


def test_add_remove_item(session: WebDriver, landing_page: InventoryPage):
    """
    1. Log into the web store -- skipped, as it's done in the setup fixture
    2. Add one product to cart in the Inventory page
    3. Verify cart items count label changed to 1
    4. Open cart
    5. Verify number of items in cart page is 1
    6. Remove item from cart
    7. Verify number of items in cart page is 0
    8. Go back to Products page
    9. Verify cart items count label changed to none
    """

    # 2. Add one product to cart in the Inventory page
    products = landing_page.products
    products[0].add_to_cart()

    # 3. Verify cart items count label changed to 1
    assert landing_page.cart_badge_num == 1, "Cart badge number doesn't match expected value"

    # 4. Open cart
    cart_page = landing_page.click_cart_button()

    # 5. Verify number of items in cart page is 1
    assert len(cart_page.items_in_cart) == 1, "Number of items in cart doesn't match expected value"

    # 6. Remove item from cart
    cart_page.items_in_cart[0].remove_from_cart()  # 0 is the index of the first product here

    # 7. Verify number of items in cart page is 0
    assert len(cart_page.items_in_cart) == 0, "Number of items in cart doesn't match expected value"

    # 8. Go back to Products page
    cart_page.click_continue_shopping()

    # 9. Verify cart items count label changed to none
    assert landing_page.cart_badge_num == 0, "Cart badge number is not empty"


def test_add_to_cart_thru_product_page(session: WebDriver, landing_page: InventoryPage):
    """
    1. Log into the web store -- skipped, as it's done in the setup fixture
    2. Open first product's page
    3. Click Add to cart
    4. Verify cart label is 1
    5. Remove item from cart
    6. Verify cart label is none
    7. Go back to products page
    """

    # 2. Open first product's page
    product_details_page = landing_page.products[0].open_product_page()

    # 3. Click Add to cart
    product_details_page.add_to_cart()

    # 4. Verify cart label is 1
    assert product_details_page.cart_badge_num == 1, "Cart badge number doesn't match expected value"

    # 5. Remove item from cart
    product_details_page.remove_from_cart()

    # 6. Verify cart label is none
    assert product_details_page.cart_badge_num == 0, "Cart badge number is not empty"

    # 7. Go back to products page
    product_details_page.back_to_products()
