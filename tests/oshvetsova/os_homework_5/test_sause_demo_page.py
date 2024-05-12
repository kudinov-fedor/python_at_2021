import pytest
from tests.oshvetsova.os_homework_5.pages.base_page import BasePage
from tests.oshvetsova.os_homework_5.pages.login_page import LogInPage
from tests.oshvetsova.os_homework_5.pages.product_page import ProductPage
from tests.oshvetsova.os_homework_5.pages.cart_page import CartPage
from tests.oshvetsova.os_homework_5.constant import HOST, USERNAME, PASSWORD, LANDING_PAGE, LOGOUT_PAGE, CART_PAGE
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture
def session():
    """
    The Incognito mode was added due to client MDM affecting browser settings
    """
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    session = webdriver.Chrome(options=chrome_options)
    yield session
    session.quit()


@pytest.fixture(autouse=True)
def login(session):
    """Verify the landing page after sucessful login"""
    login_page = LogInPage(session)
    login_page.open_page(HOST)  # navigate to the landing page
    login_page.input_creds(USERNAME, PASSWORD)  # input the credentials
    current_page_url = BasePage(session)
    assert current_page_url.get_url() == LANDING_PAGE, "The current URL does not match the expected landing page URL"


def test_product_number(session):
    """
    1. User logged in
    2. Verify that number of products on the page - expected 6
    """
    product_page = ProductPage(session)
    assert len(product_page.find_products()) == 6, "The number of products on the page does not match the expected number"


def test_user_logout(session):
    """
    1. User logged in into the webpage
    2. Open side navigation
    3. Click on "log out' button
    4. Verify that log in page is displayed
    """
    side_navigation = ProductPage(session)
    side_navigation.logout_from_system()
    current_page = LogInPage(session)

    assert current_page.get_url() == LOGOUT_PAGE, "The current URL does not match the expected logout page URL"
    assert current_page.find_username_field().is_displayed(), "The username field is not displayed"
    assert current_page.find_password_field().is_displayed(), "The password field is not displayed"


def test_delete_products_from_cart(session):
    """
    1. Adding 2 items to cart
    2. Deleting items from cart
    3. Verify current page - expected cart page
    4. Verify badge number - expected 0

    """
    product_page = ProductPage(session)
    product_page.add_to_cart(0)
    product_page.add_to_cart(1)
    product_page.open_cart()
    cart_page = CartPage(session)
    cart_page.remove_item(0)
    cart_page.remove_item(0)

    assert cart_page.get_url() == CART_PAGE, "The current URL does not match the expected cart page URL"
    assert cart_page.cart_badge() == 0, "The cart badge number does not match the expected number"
