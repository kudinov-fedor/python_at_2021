from tests.threc.HW_saucedemo.locators import CheckoutPage
from tests.threc.HW_saucedemo.locators import ProductsPage
from tests.threc.HW_saucedemo.locators import CartPage
from tests.threc.HW_saucedemo.locators import FillForm
import costants


def test_product_details(session):
    """
    Log in to the site
    Find first product
    Save the name of the first product
    Navigate to the product details page
    Check opened URL
    Compare product name from Product list page with Product details page
    """
    products = session.find_elements(*ProductsPage.listProducts)
    products[0].find_element(*ProductsPage.btnAddToCart).click()
    product_name = products[0].find_element(*ProductsPage.btnProductDetails).text
    products[0].find_element(*ProductsPage.btnProductDetails).click()

    product_details_page = session.find_element(*ProductsPage.productDetailsPage).text
    assert product_name == product_details_page

    assert session.current_url in costants.URL_PRODUCT_PAGE


def test_add_to_card(session):
    """
    Log in to the site
    Check the amount of products on the page
    Find first product
    Add this product to the cart
    Check the amount of added products to the card by amount on the badge
    """
    products = session.find_elements(*ProductsPage.listProducts)
    assert len(products) == costants.PRODUCT_LENGTH

    products[0].find_element(*ProductsPage.btnAddToCart).click()

    cart = session.find_element(*CartPage.shoppingCart)
    cart_badge = cart.find_element(*CartPage.cartBadge)
    assert cart_badge.text == costants.CART_BADGE


def test_add_all_cart(session):
    """
    Log in to the site
    Find all product
    Add all product to the cart
    Check the amount of added products to the cart by amount on the badge
    """
    products = session.find_elements(*ProductsPage.listProducts)
    for i in range(costants.PRODUCT_LENGTH):
        products[i].find_element(*ProductsPage.btnAddToCart).click()

    cart = session.find_element(*CartPage.shoppingCart)
    cart_badge = cart.find_element(*CartPage.cartBadge)
    assert cart_badge.text == costants.CART_BADGE_ALL_PRODUCTS


def test_navigation_to_cart(session):
    """
    Log in to the site
    Find fist product
    Add it to the cart
    Open cart page
    Compare name of added product from the cart with the name of the product from the products page
    """
    products = session.find_elements(*ProductsPage.listProducts)
    products[0].find_element(*ProductsPage.btnAddToCart).click()
    product_name = products[0].find_element(*ProductsPage.btnProductDetails).text

    assert product_name == costants.PRODUCT_NAME

    cart = session.find_element(*CartPage.shoppingCart)
    cart.find_element(*CartPage.cartBadge).click()
    cart_product_name = session.find_element(*CartPage.cartProductName).text
    assert product_name == cart_product_name


def test_continue_shopping(session):
    """
    Log in to the site
    Find first product
    Add it to the cart
    Click on the Continue shopping button
    Check the navigation to the Product page
    """
    products = session.find_elements(*ProductsPage.listProducts)
    products[0].find_element(*ProductsPage.btnAddToCart).click()

    cart = session.find_element(*CartPage.shoppingCart)
    cart.find_element(*CartPage.cartBadge).click()

    session.find_element(*CheckoutPage.btnContinueShopping).click()
    assert session.current_url in costants.URL_MAIN_PRODUCT_PAGE


def test_navigate_checkout(session):
    """
    Log in to the site
    Add first product to the cart
    Click on the Checkout button
    Check that the Checkout step first is opened
    """
    products = session.find_elements(*ProductsPage.listProducts)
    products[0].find_element(*ProductsPage.btnAddToCart).click()

    cart = session.find_element(*CartPage.shoppingCart)
    cart.find_element(*CartPage.cartBadge).click()

    session.find_element(*CheckoutPage.btnCheckout).click()
    assert session.current_url in costants.URL_CHECKOUT_STEP_ONE


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
    products = session.find_elements(*ProductsPage.listProducts)
    products[0].find_element(*ProductsPage.btnAddToCart).click()
    product_name = products[0].find_element(*ProductsPage.btnProductDetails).text
    assert product_name == costants.PRODUCT_NAME

    cart = session.find_element(*CartPage.shoppingCart)
    cart.find_element(*CartPage.cartBadge).click()

    session.find_element(*CheckoutPage.btnCheckout).click()

    session.find_element(*FillForm.firstName).send_keys(costants.FIRST_NAME)
    session.find_element(*FillForm.lastName).send_keys(costants.LAST_NAME)
    session.find_element(*FillForm.zipCode).send_keys(costants.ZIPCODE)

    session.find_element(*FillForm.btnContinue).click()

    checkout_item = session.find_element(*CheckoutPage.checkoutItem).text

    assert product_name == checkout_item

    session.find_element(*FillForm.btnFinish).click()
    finish_title = session.find_element(*FillForm.finishOrderTitle).text
    assert finish_title == costants.COMPLETE_CHECKOUT

    assert session.current_url in costants.URL_FINISH_CHECKOUT
