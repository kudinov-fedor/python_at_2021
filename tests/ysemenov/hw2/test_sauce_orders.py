from selenium.webdriver import Chrome
from selenium.common import NoSuchElementException
from tests.ysemenov.hw3.locators import *
import pytest

HOST = "https://www.saucedemo.com"
LOGIN = "standard_user"
PASSWORD = "secret_sauce"


@pytest.fixture(scope="function")
def session():
    session = Chrome()
    yield session

    # tear down
    session.quit()


def test_order_product(session):
    """
    1. Log into the web store
    2. Add one product to cart
    3. Open cart
    4. Verify number of items added is 1
    5. Navigate to Checkout
    6. Fill in details and click Continue
    7. Finish the order
    8. Check that the order was successful
    """
    session.get(HOST)

    # 1. Log into the web store
    session.find_element(*LoginPage.txtLogin).send_keys(LOGIN)
    session.find_element(*LoginPage.txtPassword).send_keys(PASSWORD)
    session.find_element(*LoginPage.btnSubmit).click()

    # 2. Add one product to cart in the Inventory page
    elements = session.find_elements(*InventoryPage.lstInventory)
    elements[0].find_element(*InventoryPage.btnAddToCart).click()

    # 3. Open cart by clicking Cart button
    cart = session.find_element(*HeaderMenu.btnCart)
    cart.click()

    # 4. Verify number of items added is 1
    items = session.find_elements(*CartPage.lstCartItems)
    assert len(items) == 1

    # 5. Click Checkout to navigate to Checkout page
    session.find_element(*CartPage.btnCheckout).click()

    # 6. Fill in details and click Continue
    session.find_element(*CheckoutPage.txtFirstName).send_keys("Luke")
    session.find_element(*CheckoutPage.txtLastName).send_keys("Skywalker")
    session.find_element(*CheckoutPage.txtPostalCode).send_keys("90210")
    session.find_element(*CheckoutPage.btnContinue).click()

    # 7. Finish the order
    session.find_element(*OverviewPage.btnFinish).click()

    # 8. Check that the order was successful
    title_complete = session.find_element(*CompletePage.headerComplete).text
    assert title_complete == "Thank you for your order!"


def test_add_remove_item(session):
    """
    1. Log into the web store
    2. Add one product to cart
    3. Verify cart label changed to 1
    4. Open cart
    5. Verify number of items in cart is 1
    6. Remove item from cart
    7. Verify number of items in cart is 0
    8. Go back to products page
    9. Verify cart label changed to none
    """
    session.get(HOST)

    # 1. Log into the web store
    session.find_element(*LoginPage.txtLogin).send_keys(LOGIN)
    session.find_element(*LoginPage.txtPassword).send_keys(PASSWORD)
    session.find_element(*LoginPage.btnSubmit).click()

    # 2. Add one product to cart in the Inventory page
    elements = session.find_elements(*InventoryPage.lstInventory)
    elements[0].find_element(*InventoryPage.btnAddToCart).click()

    # 3. Verify cart items count label changed to 1
    cart = session.find_element(*HeaderMenu.btnCart)
    cart_badge = cart.find_element(*HeaderMenu.cartBadge)
    assert cart_badge.text == '1'

    # 4. Open cart
    cart.click()

    # 5. Verify number of items in cart page is 1
    items = session.find_elements(*CartPage.lstCartItems)
    assert len(items) == 1

    # 6. Remove item from cart
    session.find_element(*CartPage.btnRemoveFromCart).click()

    # 7. Verify number of items in cart page is 0
    items = session.find_elements(*CartPage.lstCartItems)
    assert len(items) == 0

    # 8. Go back to Products page
    session.find_element(*CartPage.btnContinueShopping).click()

    # 9. Verify cart items count label changed to none
    cart = session.find_element(*HeaderMenu.btnCart)

    with pytest.raises(NoSuchElementException):
        cart.find_element(*HeaderMenu.cartBadge)


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
    session.get(HOST)

    # 1. Log into the web store
    session.find_element(*LoginPage.txtLogin).send_keys(LOGIN)
    session.find_element(*LoginPage.txtPassword).send_keys(PASSWORD)
    session.find_element(*LoginPage.btnSubmit).click()

    # 2. Open first product's description page
    elements = session.find_elements(*InventoryPage.lstInventory)
    elements[0].find_element(*InventoryPage.lnkProductName).click()

    # 3. Click Add to cart in the product description page
    session.find_element(*ProductDescriptionPage.btnAddToCart).click()

    # 4. Verify cart label is 1
    cart = session.find_element(*HeaderMenu.btnCart)
    cart_badge = cart.find_element(*HeaderMenu.cartBadge)
    assert cart_badge.text == '1'

    # 5. Remove item from cart in the product description page
    session.find_element(*ProductDescriptionPage.btnRemove).click()

    # 6. Verify cart items count label is null
    cart = session.find_element(*HeaderMenu.btnCart)

    with pytest.raises(NoSuchElementException):
        cart.find_element(*HeaderMenu.cartBadge)

    # 7. Go back to products page
    session.find_element(*ProductDescriptionPage.btnBackToProducts).click()
