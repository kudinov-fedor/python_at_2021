from tests.threc.hw6.page_object.product_page import ProductPage
from tests.threc.hw6.page_object.product_details_page import ProductDetailsPage
from tests.threc.hw6.page_object.finish_page import FinishPage
from tests.threc.hw6.page_object.cart_page import CartPage
from tests.threc.hw6.page_object.checkout_page import CheckoutPage
import constants


def test_product_details(driver):
    """
    Log in to the site
    Find first product
    Save the name of the first product
    Navigate to the product details page
    Check opened URL
    Compare product name from Product list page with Product details page
    """
    products = ProductPage(driver).get_list_products()
    assert len(products) == 6

    product_name = products[0].get_name()
    products[0].go_to_details()

    product_details_name = ProductDetailsPage(driver).get_product_name()
    assert product_name == product_details_name

    assert driver.current_url in constants.URL_PRODUCT_PAGE


def test_add_to_card(driver):
    """
    Log in to the site
    Check the amount of products on the page
    Find first product
    Add this product to the cart
    Check the amount of added products to the card by amount on the badge
    """
    product_page = ProductPage(driver)
    products = product_page.get_list_products()
    assert len(products) == constants.PRODUCT_LENGTH

    products[0].add_to_cart()
    badge_value = product_page.get_badge_value()
    assert badge_value == constants.CART_BADGE


def test_add_all_cart(driver):
    """
    Log in to the site
    Find all product
    Add all product to the cart
    Check the amount of added products to the cart by amount on the badge
    """
    product_page = ProductPage(driver)
    products = product_page.get_list_products()

    for i in products:
        i.add_to_cart()

    badge_value = product_page.get_badge_value()
    assert badge_value == constants.CART_BADGE_ALL_PRODUCTS


def test_navigation_to_cart(driver):
    """
    Log in to the site
    Find fist product
    Add it to the cart
    Open cart page
    Compare name of added product from the cart with the name of the product from the products page
    """
    product_page = ProductPage(driver)
    products = product_page.get_list_products()
    products[0].add_to_cart()

    product_name = products[0].get_name()
    assert product_name == constants.PRODUCT_NAME

    product_page.open_cart()
    cart_page = CartPage(driver)
    added_products = cart_page.get_products()
    cart_product_name = added_products[0].get_name()
    assert cart_product_name == product_name


def test_continue_shopping(driver):
    """
    Log in to the site
    Find first product
    Add it to the cart
    Click on the Continue shopping button
    Check the navigation to the Product page
    """
    product_page = ProductPage(driver)
    products = product_page.get_list_products()
    products[0].add_to_cart()
    product_page.open_cart()
    CartPage(driver).click_continue_btn()
    assert driver.current_url in constants.URL_MAIN_PRODUCT_PAGE


def test_navigate_checkout(driver):
    """
    Log in to the site
    Add first product to the cart
    Click on the Checkout button
    Check that the Checkout step first is opened
    """
    product_page = ProductPage(driver)
    product_page.open_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout_btn()
    assert driver.current_url in constants.URL_CHECKOUT_STEP_ONE


def test_fill_order_form(driver):
    """
    Log in to the site
    Add first product to the cart
    Click on the Checkout button
    Fill the checkout form
    Click on teh Continue button
    Compare added element with the element on the Checkout:Overview page
    Click on the Finish button
    Check that the Finish page is opened
    """
    product_page = ProductPage(driver)
    products = product_page.get_list_products()
    product_name = products[0] \
        .add_to_cart()  \
        .get_name()
    assert product_name == constants.PRODUCT_NAME

    product_page.open_cart()
    cart_page = CartPage(driver)
    cart_page.click_checkout_btn()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form(constants.FIRST_NAME, constants.LAST_NAME, constants.ZIPCODE)
    checkout_page.click_submit_btn()

    added_products = checkout_page.get_added_products()
    overview_product_name = added_products[0].get_name()
    assert product_name == overview_product_name

    checkout_page.click_finish_btn()
    finish_title = FinishPage(driver).get_finish_order_title()
    assert finish_title == constants.COMPLETE_CHECKOUT

    assert driver.current_url in constants.URL_FINISH_CHECKOUT


def test_cart_is_empty_after_login(driver):
    """
    login
    click on the cart
    check cart is empty
    """
    badge_value = ProductPage(driver).get_badge_value()
    assert badge_value == constants.CART_EMPTY_BADGE
