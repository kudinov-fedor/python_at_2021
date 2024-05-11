from tests.ysemenov.hw5 import pages
from tests.ysemenov.hw5.conftest import LOGIN, PASSWORD, FIRSTNAME, LASTNAME, POSTALCODE, MESSAGE_SUCCESS


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

    base_page = pages.BasePage(session)
    base_page.open()

    # LOGIN PAGE
    # 1. Log into the web store
    login_page = pages.LoginPage(session)
    login_page.log_in(LOGIN, PASSWORD)

    # session.find_element(*locators.LoginPage.TXT_LOGIN).send_keys(LOGIN)
    # session.find_element(*locators.LoginPage.TXT_PASSWORD).send_keys(PASSWORD)
    # session.find_element(*locators.LoginPage.BTN_SUBMIT).click()

    # INVENTORY PAGE
    # 2. Add to cart first product in the Inventory page
    # elements = base_page.find_elements(*locators.InventoryPage.LST_INVENTORY)
    # elements[0].find_element(*locators.InventoryPage.BTN_ADD_TO_CART).click()
    inventory_page = pages.InventoryPage(session)
    inventory_page.add_product_to_cart(inventory_page.get_products()[0])  # 0 is the index of the first product

    # HEADER MENU
    # 3. Open cart by clicking Cart button
    # cart = session.find_element(*locators.LocatorsHeaderMenu.BTN_CART)
    # cart.click()
    base_page.click_cart_button()

    # CART PAGE
    # 4. Verify number of items added is 1
    # items = session.find_elements(*locators.LocatorsCartPage.LST_CART_ITEMS)
    # assert len(items) == 1
    cart_page = pages.CartPage(session)
    assert len(cart_page.get_items_in_cart()) == 1, "Number of items in cart doesn't match expected value"

    # 5. Click Checkout to navigate to Checkout page
    cart_page.click_checkout()

    # CHECKOUT PAGE
    # 6. Fill in details and click Continue
    # session.find_element(*locators.LocatorsCheckoutPage.TXT_FIRST_NAME).send_keys("Luke")
    # session.find_element(*locators.LocatorsCheckoutPage.TXT_LAST_NAME).send_keys("Skywalker")
    # session.find_element(*locators.LocatorsCheckoutPage.TXT_POSTAL_CODE).send_keys("90210")
    # session.find_element(*locators.LocatorsCheckoutPage.BTN_CONTINUE).click()
    checkout_page = pages.CheckoutPage(session)
    checkout_page.submit_checkout_details(FIRSTNAME, LASTNAME, POSTALCODE)

    # OVERVIEW PAGE
    # 7. Finish the order
    # session.find_element(*locators.LocatorsOverviewPage.BTN_FINISH).click()
    overview_page = pages.OverviewPage(session)
    overview_page.finish_order()

    # COMPLETE PAGE
    # 8. Check that the order was successful
    # title_complete = session.find_element(*locators.LocatorsCompletePage.HEADER_COMPLETE).text
    # assert title_complete == "Thank you for your order!"
    order_status_page = pages.OrderStatusPage(session)
    assert order_status_page.get_order_msg() == MESSAGE_SUCCESS, "Message doesn't match expected value"


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

    base_page = pages.BasePage(session)
    base_page.open()

    # LOGIN PAGE
    # 1. Log into the web store
    # session.find_element(*locators.LoginPage.TXT_LOGIN).send_keys(LOGIN)
    # session.find_element(*locators.LoginPage.TXT_PASSWORD).send_keys(PASSWORD)
    # session.find_element(*locators.LoginPage.BTN_SUBMIT).click()
    login_page = pages.LoginPage(session)
    login_page.log_in(LOGIN, PASSWORD)

    # INVENTORY PAGE
    # 2. Add one product to cart in the Inventory page
    # elements = session.find_elements(*locators.LocatorsInventoryPage.LST_INVENTORY)
    # elements[0].find_element(*locators.LocatorsInventoryPage.BTN_ADD_TO_CART).click()
    inventory_page = pages.InventoryPage(session)
    inventory_page.add_product_to_cart(inventory_page.get_products()[0])  # 0 is the index of the first product

    # HEADER MENU
    # 3. Verify cart items count label changed to 1
    # cart = session.find_element(*locators.LocatorsHeaderMenu.BTN_CART)
    # cart_badge = cart.find_element(*locators.LocatorsHeaderMenu.CART_BADGE)
    # assert cart_badge.text == '1'
    cart_badge_number = base_page.get_cart_badge_number()
    assert cart_badge_number == 1, "Cart badge number doesn't match expected value"

    # 4. Open cart
    # cart.click()
    base_page.click_cart_button()

    # CART PAGE
    # 5. Verify number of items in cart page is 1
    # items = session.find_elements(*locators.LocatorsCartPage.LST_CART_ITEMS)
    # assert len(items) == 1
    cart_page = pages.CartPage(session)
    assert len(cart_page.get_items_in_cart()) == 1, "Number of items in cart doesn't match expected value"

    # 6. Remove item from cart
    # session.find_element(*locators.LocatorsCartPage.BTN_REMOVE_FROM_CART).click()
    cart_page.remove_from_cart(cart_page.get_items_in_cart()[0])  # 0 is the index of the first product here

    # 7. Verify number of items in cart page is 0
    # items = session.find_elements(*locators.LocatorsCartPage.LST_CART_ITEMS)
    # assert len(items) == 0
    cart_page = pages.CartPage(session)
    assert len(cart_page.get_items_in_cart()) == 0, "Number of items in cart doesn't match expected value"

    # 8. Go back to Products page
    # session.find_element(*locators.LocatorsCartPage.BTN_CONTINUE_SHOPPING).click()
    cart_page.click_continue_shopping()

    # HEADER MENU
    # 9. Verify cart items count label changed to none
    # cart = session.find_element(*locators.LocatorsHeaderMenu.BTN_CART)
    #
    # with pytest.raises(NoSuchElementException):
    #     cart.find_element(*locators.LocatorsHeaderMenu.CART_BADGE)
    cart_badge_number = base_page.get_cart_badge_number()
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

    base_page = pages.BasePage(session)
    base_page.open()

    # LOGIN PAGE
    # 1. Log into the web store
    # session.find_element(*locators.LocatorsLoginPage.TXT_LOGIN).send_keys(LOGIN)
    # session.find_element(*locators.LocatorsLoginPage.TXT_PASSWORD).send_keys(PASSWORD)
    # session.find_element(*locators.LocatorsLoginPage.BTN_SUBMIT).click()
    login_page = pages.LoginPage(session)
    login_page.log_in(LOGIN, PASSWORD)

    # INVENTORY PAGE
    # 2. Open first product's description page
    # elements = session.find_elements(*locators.LocatorsInventoryPage.LST_INVENTORY)
    # elements[0].find_element(*locators.LocatorsInventoryPage.LNK_PRODUCT_NAME).click()
    inventory_page = pages.InventoryPage(session)
    inventory_page.open_product_page(inventory_page.get_products()[0])  # 0 is the index of the first product here

    # PRODUCT DESCRIPTION PAGE
    # 3. Click Add to cart in the product description page
    # session.find_element(*locators.LocatorsProductDetailsPage.BTN_ADD_TO_CART).click()
    product_details_page = pages.ProductDetailsPage(session)
    product_details_page.add_to_cart()

    # HEADER MENU
    # 4. Verify cart label is 1
    # cart = session.find_element(*locators.LocatorsHeaderMenu.BTN_CART)
    # cart_badge = cart.find_element(*locators.LocatorsHeaderMenu.CART_BADGE)
    # assert cart_badge.text == '1'
    cart_badge_number = base_page.get_cart_badge_number()
    assert cart_badge_number == 1, "Cart badge number doesn't match expected value"

    # PRODUCT DESCRIPTION PAGE
    # 5. Remove item from cart in the product description page
    # session.find_element(*locators.LocatorsProductDetailsPage.BTN_REMOVE).click()
    product_details_page.remove_from_cart()

    # HEADER MENU
    # 6. Verify cart items count label is null
    # cart = session.find_element(*locators.LocatorsHeaderMenu.BTN_CART)
    #
    # with pytest.raises(NoSuchElementException):
    #     cart.find_element(*locators.LocatorsHeaderMenu.CART_BADGE)
    cart_badge_number = base_page.get_cart_badge_number()
    assert cart_badge_number == 0, "Cart badge number is not empty"

    # PRODUCT DESCRIPTION PAGE
    # 7. Go back to products page
    # session.find_element(*locators.LocatorsProductDetailsPage.BTN_BACK_TO_PRODUCTS).click()
    product_details_page.back_to_products()
