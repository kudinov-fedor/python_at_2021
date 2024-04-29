from tests.threc.hw5_saucedemo_oop.locators import LocProductsPage
from tests.threc.hw5_saucedemo_oop.page_object.product_page import ProductPage
from tests.threc.hw5_saucedemo_oop.page_object.product_details_page import ProductDetailsPage
from tests.threc.hw5_saucedemo_oop.page_object.cart_page import CartPage
from tests.threc.hw5_saucedemo_oop.page_object.checkout_page import CheckoutPage
from tests.threc.hw5_saucedemo_oop.page_object.finish_page import FinishPage
import constants


def test_product_details(session):
    """
    Log in to the site
    Find first product
    Save the name of the first product
    Navigate to the product details page
    Check opened URL
    Compare product name from Product list page with Product details page
    """
    products = ProductPage(session)
    products.list_products()

    item = products.line_product(0)
    products.add_to_cart(item)

    product_name = products.product_label(item)
    products.product_details(item)

    details = ProductDetailsPage(session)
    product_details_page = details.product_details_label()
    assert product_name == product_details_page

    assert session.current_url in constants.URL_PRODUCT_PAGE


def test_add_to_card(session):
    """
    Log in to the site
    Check the amount of products on the page
    Find first product
    Add this product to the cart
    Check the amount of added products to the card by amount on the badge
    """
    products = ProductPage(session)
    items = products.list_products()
    assert len(items) == constants.PRODUCT_LENGTH

    item = products.line_product(0)
    products.add_to_cart(item)

    cart = CartPage(session)
    cart_item = cart.shopping_cart_badge()
    cart_badge = cart.cart_badge_label(cart_item)

    assert cart_badge == constants.CART_BADGE


def test_add_all_cart(session):
    """
    Log in to the site
    Find all product
    Add all product to the cart
    Check the amount of added products to the cart by amount on the badge
    """
    products = ProductPage(session)
    products.list_products()

    for i in range(constants.PRODUCT_LENGTH):
        item = products.line_product(i)
        products.add_to_cart(item)

    cart = CartPage(session)
    cart_item = cart.shopping_cart_badge()
    cart_badge = cart.cart_badge_label(cart_item)
    assert cart_badge == constants.CART_BADGE_ALL_PRODUCTS


def test_navigation_to_cart(session):
    """
    Log in to the site
    Find fist product
    Add it to the cart
    Open cart page
    Compare name of added product from the cart with the name of the product from the products page
    """
    products = ProductPage(session)
    products.list_products()

    item = products.line_product(0)
    products.add_to_cart(item)

    product_name = products.product_label(item)

    assert product_name == constants.PRODUCT_NAME

    cart = CartPage(session)
    cart_item = cart.shopping_cart_badge()
    cart.btn_click(cart_item)
    assert cart.cart_product_name() == product_name


def test_continue_shopping(session):
    """
    Log in to the site
    Find first product
    Add it to the cart
    Click on the Continue shopping button
    Check the navigation to the Product page
    """
    products = ProductPage(session)
    products.list_products()

    item = products.line_product(0)
    products.add_to_cart(item)

    cart = CartPage(session)
    cart_item = cart.shopping_cart_badge()
    cart.btn_click(cart_item)
    cart.btn_click(cart.cart_continue_btn())
    assert session.current_url in constants.URL_MAIN_PRODUCT_PAGE


def test_navigate_checkout(session):
    """
    Log in to the site
    Add first product to the cart
    Click on the Checkout button
    Check that the Checkout step first is opened
    """
    products = ProductPage(session)
    products.list_products()

    item = products.line_product(0)
    products.add_to_cart(item)

    cart = CartPage(session)
    cart_item = cart.shopping_cart_badge()
    cart.btn_click(cart_item)
    cart.btn_click(cart.cart_checkout_btn())

    assert session.current_url in constants.URL_CHECKOUT_STEP_ONE


def test_fill_order_form(session):
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
    products = ProductPage(session)
    items = products.list_products()

    item = products.line_product(0)
    products.add_to_cart(item)

    product_name = items[0].find_element(*LocProductsPage.btnProductDetails).text
    assert product_name == constants.PRODUCT_NAME

    cart = CartPage(session)
    cart_item = cart.shopping_cart_badge()
    cart.btn_click(cart_item)
    cart.btn_click(cart.cart_checkout_btn())

    checkout = CheckoutPage(session)
    checkout.checkout_fill_form(constants.FIRST_NAME, constants.LAST_NAME, constants.ZIPCODE)
    checkout.checkout_btn_click(checkout.checkout_submit_btn())
    checkout_item = checkout.checkout_product_label()
    assert product_name == checkout_item

    checkout.checkout_btn_click(checkout.checkout_finish_btn())
    finish = FinishPage(session)
    finish_title = finish.finish_title()
    assert finish_title == constants.COMPLETE_CHECKOUT

    assert session.current_url in constants.URL_FINISH_CHECKOUT
