import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from tests. oshvetsova. os_homework_3.locators import (
    LogIn,
    AddItems,
    ShoppingCart)


HOST = "https://www.saucedemo.com"
LOGIN = "standard_user"
PASSWORD = "secret_sauce"


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
def user_login(session):
    session.get(HOST)

    # вхід в систему
    session.find_element(*LogIn.USER_NAME).send_keys(LOGIN)
    session.find_element(*LogIn.PASSWORD).send_keys(PASSWORD)
    session.find_element(*LogIn.BTN_LOGIN).click()


@pytest.fixture
@pytest.mark.usefixtures("user_login")
def cart_with_2_items(session):
    """
    1. Check the number of available products on the page
    2. Add 2 products to cart
    """

    elements = session.find_elements(*AddItems.INVENTORY_ITEMS)
    assert len(elements) == 6

    elements[0].find_element(*AddItems.BTN_ADD_TO_CART).click()
    elements[2].find_element(*AddItems.BTN_ADD_TO_CART).click()


@pytest.mark.usefixtures("cart_with_2_items")
def test_main_flow(session):
    """
    1. Check cart icon
    2. Open cart
    3. Verify the number of items in cart (expected 2 items)
    4. Navigate to checkout page
    5. Enter checkout information
    6. Verify that cart icon doesn't have a number
    """

    # перевірити індикатор корзини
    cart = session.find_element(*ShoppingCart.CART_CONTAINER)
    cart_badge = cart.find_element(*ShoppingCart.CART_BADGE)
    assert cart_badge.text == "2"

    # перейти в корзину
    cart.click()

    # перевірити кількість елементів в корзині
    items = session.find_elements(*ShoppingCart.CART_LIST)
    assert len(items) == 2

    # перейти до оформлення замовлення
    session.find_element(*ShoppingCart.BTN_CHECKOUT).click()

    # заповнення форми замовлення
    session.find_element(*ShoppingCart.FIRST_NAME).send_keys("Jonh")
    session.find_element(*ShoppingCart.LAST_NAME).send_keys("Adams")
    session.find_element(*ShoppingCart.POSTAL_CODE).send_keys("001011")
    session.find_element(*ShoppingCart.BTN_CONTINUE).click()

    # виконати замовлення
    session.find_element(*ShoppingCart.BTN_FINISH).click()

    # перевірити, що корзина пуста
    session.find_element(*ShoppingCart.BACK_TO_PRODUCT).click()
    cart = session.find_element(*ShoppingCart.CART_CONTAINER)

    with pytest.raises(NoSuchElementException):
        cart.find_element(*ShoppingCart.CART_BADGE)


@pytest.mark.usefixtures("cart_with_2_items")
def test_removing_added_product(session):
    """
    1. Open cart page
    2. Verify the number of items it cart
    3. Remove one product
    4. Verify the number of product added in cart
    """

    # перевірити індикатор корзини
    cart = session.find_element(*ShoppingCart.CART_CONTAINER)
    cart_badge = cart.find_element(*ShoppingCart.CART_BADGE)
    assert cart_badge.text == "2"

    # перейти в корзину
    cart.click()

    # перевірити кількість елементів в корзині
    items = session.find_elements(*ShoppingCart.CART_LIST)
    assert len(items) == 2

    # delete element
    items[0].find_element(*ShoppingCart.REMOVE_ITEM).click()

    # перевірити кількість елементів в корзині
    items = session.find_elements(*ShoppingCart.CART_LIST)
    assert len(items) == 1


@pytest.fixture
def login_and_go_to_cart(session):

    # перейти в корзину
    cart = session.find_element(*ShoppingCart.CART_CONTAINER)
    cart.click()

def test_checkout_disabled_if_cart_empty(session, login_and_go_to_cart):
    """
    Verify that the checkout button is disabled
    """

    # перевірити кількість елементів в корзині
    items = session.find_elements(*ShoppingCart.CART_LIST)
    assert len(items) == 0

    checkout_button = session.find_element(*ShoppingCart.BTN_CHECKOUT).is_enabled()
    assert checkout_button == False
