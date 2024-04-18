import pytest
from selenium.common import NoSuchElementException
from tests.mariana_petrushanska.test_selenium_hw_2 import constants
from tests.mariana_petrushanska.test_selenium_hw_2.locators import CartItems
from tests.mariana_petrushanska.test_selenium_hw_2.locators import InformationPage
from tests.mariana_petrushanska.test_selenium_hw_2.locators import OverviewPage
from tests.mariana_petrushanska.test_selenium_hw_2.locators import SuccessPage


def test_no_order_with_0_items_possible(session):
    """
    Check that cart is empty when user logs in:
    1. Log in (covered with "login" fixture).
    2. Click on the cart item.
    3. Check number of items in the cart.
    4. Check that 'Checkout' button is disabled.
    """

    # 2. Click on the cart item.
    cart = session.find_element(*CartItems.IMG_CART)
    cart.click()

    # 3. Check number of items in the cart.
    items = session.find_elements(*CartItems.LST_CART_ITEMS)
    assert len(items) == 0

    # 4. Check that 'Checkout' button is disabled.
    checkout = session.find_element(*CartItems.BTN_CHECKOUT).is_enabled()
    assert checkout is False


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
    cart = session.find_element(*CartItems.IMG_CART)
    cart_badge = cart.find_element(*CartItems.IMG_CART_BADGE)
    assert cart_badge.text == '3'

    # 5. Go to cart.
    cart.click()

    # 6. Check number of items in the cart.
    items = session.find_elements(*CartItems.LST_CART_ITEMS)
    assert len(items) == 3

    # 7. Click on 'Checkout' button.
    session.find_element(*CartItems.BTN_CHECKOUT).click()

    # 8. Fill in user's information.
    session.find_element(*InformationPage.TXT_FIRST_NAME).send_keys(constants.FIRST_NAME)
    session.find_element(*InformationPage.TXT_LAST_NAME).send_keys(constants.LAST_NAME)
    session.find_element(*InformationPage.TXT_POSTAL_CODE).send_keys(constants.POSTAL_CODE)

    # 9. Click on 'Continue' button.
    session.find_element(*InformationPage.BTN_CONTINUE).click()

    # 10. Click on 'Finish' button.
    session.find_element(*OverviewPage.BTN_FINISH).click()

    # 11. Click on 'Back Home' button on 'Success' page.
    session.find_element(*SuccessPage.BTN_BACK_HOME).click()

    # 12. Check that the cart is empty.
    cart = session.find_element(*CartItems.IMG_CART)

    with pytest.raises(NoSuchElementException):
        cart.find_element(*CartItems.IMG_CART_BADGE)


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
    cart = session.find_element(*CartItems.IMG_CART)
    cart_badge = cart.find_element(*CartItems.IMG_CART_BADGE)
    assert cart_badge.text == '3'

    # 5. Go to cart.
    cart.click()

    # 6. Check number of items in the cart.
    items = session.find_elements(*CartItems.LST_CART_ITEMS)
    assert len(items) == 3

    # 7. Remove 2nd item.
    items[1].find_element(*CartItems.BTN_REMOVE_SECOND_ITEM).click()

    # 8. Check number of items in the cart to make sure it is updated accordingly.
    items = session.find_elements(*CartItems.LST_CART_ITEMS)
    assert len(items) == 2


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
    cart = session.find_element(*CartItems.IMG_CART)
    cart.click()

    # 5. Click on 'Checkout' button.
    session.find_element(*CartItems.BTN_CHECKOUT).click()

    # 6. Fill in user's information.
    session.find_element(*InformationPage.TXT_FIRST_NAME).send_keys(constants.FIRST_NAME)
    session.find_element(*InformationPage.TXT_LAST_NAME).send_keys(constants.LAST_NAME)
    session.find_element(*InformationPage.TXT_POSTAL_CODE).send_keys(constants.POSTAL_CODE)

    # 7. Click on 'Continue' button.
    session.find_element(*InformationPage.BTN_CONTINUE).click()

    # 8. Calculate the sum of all items' prices.
    item_price = []
    item_price = session.find_elements(*OverviewPage.TXT_ITEM_PRICE)
    prices = []
    prices = [item.text for item in item_price]
    final_item_price = []
    final_item_price = [float(price.replace('$', '')) for price in prices]
    calculated_total = sum(final_item_price)

    # 9. Check that calculated sum = 'Item total' value on the page.
    item_total = session.find_element(*OverviewPage.TXT_ITEM_TOTAL).text
    item_total = float(item_total.replace('Item total: $', ''))
    assert item_total == calculated_total
