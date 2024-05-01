import pytest
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException


HOST = "https://www.saucedemo.com/"
user_name = "standard_user"
user_pass = "secret_sauce"


@pytest.fixture
def open_session():
    session = Chrome()
    session.get(HOST)

    yield session

    session.quit()


@pytest.fixture(autouse=True)
def login(open_session):
    open_session.find_element(By.ID, "user-name").send_keys(user_name)
    open_session.find_element(By.CSS_SELECTOR, "#password").send_keys(user_pass)
    open_session.find_element(By.CSS_SELECTOR, "input.submit-button.btn_action").click()


def test_basic_flow(open_session):
    """
    Check number of items on page
    add 1 item to cart from landing page
    check cart badge is updated
    check element is added to cart
    check Continue Shopping button
    open another item
    add to card
    check cart badge is updated
    open cart and check it has 2 items
    checkout and confirm
    """
    elements = open_session.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
    assert len(elements) == 6

    elements[0].find_element(By.CSS_SELECTOR, ".btn").click()
    cart = open_session.find_element(By.ID, "shopping_cart_container")
    cart_badge = cart.find_element(By.CSS_SELECTOR, ".shopping_cart_badge[data-test='shopping-cart-badge']")
    assert cart_badge.text == '1'
    cart.click()
    assert len(open_session.find_elements(By.CSS_SELECTOR, ".cart_item")) == 1
    open_session.find_element(By.CSS_SELECTOR, ".btn[data-test='continue-shopping']").click()

    elements = open_session.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
    elements[5].find_element(By.CSS_SELECTOR, ".inventory_item_name").click()
    assert "?id=" in str(open_session.current_url)
    open_session.find_element(By.CSS_SELECTOR, ".btn[data-test='add-to-cart']").click()
    cart = open_session.find_element(By.ID, "shopping_cart_container")
    cart_badge = cart.find_element(By.CSS_SELECTOR, ".shopping_cart_badge[data-test='shopping-cart-badge']")
    assert cart_badge.text == '2'
    cart.click()
    assert len(open_session.find_elements(By.CSS_SELECTOR, ".cart_item")) == 2

    open_session.find_element(By.CSS_SELECTOR, "#checkout").click()
    open_session.find_element(By.CSS_SELECTOR, "#first-name").send_keys("1")
    open_session.find_element(By.CSS_SELECTOR, "#last-name").send_keys("2")
    open_session.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("3")
    open_session.find_element(By.CSS_SELECTOR, ".btn[data-test='continue']").click()
    open_session.find_element(By.CSS_SELECTOR, ".btn[data-test='finish']").click()


def test_delete_items(open_session):
    elements = open_session.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
    cart = open_session.find_element(By.ID, "shopping_cart_container")

    elements[0].find_element(By.CSS_SELECTOR, ".btn").click()
    elements[1].find_element(By.CSS_SELECTOR, ".btn").click()
    elements[2].find_element(By.CSS_SELECTOR, ".btn").click()
    cart_badge = cart.find_element(By.CSS_SELECTOR, ".shopping_cart_badge[data-test='shopping-cart-badge']")
    assert cart_badge.text == '3'

    elements[2].find_element(By.CSS_SELECTOR, ".btn").click()
    assert cart_badge.text == '2'

    elements[1].find_element(By.CSS_SELECTOR, ".inventory_item_name").click()

    open_session.find_element(By.CSS_SELECTOR, "#remove").click()
    cart = open_session.find_element(By.ID, "shopping_cart_container")
    cart_badge = cart.find_element(By.CSS_SELECTOR, ".shopping_cart_badge[data-test='shopping-cart-badge']")
    assert cart_badge.text == '1'

    cart.click()

    cart_item = open_session.find_element(By.CSS_SELECTOR, ".cart_item")
    cart_item.find_element(By.CSS_SELECTOR, ".btn").click()
    assert len(open_session.find_elements(By.CSS_SELECTOR, ".cart_item")) == 0


def test_cart_is_empty(open_session):
    cart = open_session.find_element(By.ID, "shopping_cart_container")
    with pytest.raises(NoSuchElementException):
        open_session.find_element(By.CSS_SELECTOR, ".shopping_cart_badge[data-test='shopping-cart-badge']")
    cart.click()
    with pytest.raises(NoSuchElementException):
        open_session.find_element(By.CSS_SELECTOR, ".cart_item")
    # TODO
#    checkout_button = open_session.find_element(By.CSS_SELECTOR, "#checkout")
#    assert not checkout_button.is_enabled()


def test_logout(open_session):
    assert len(open_session.get_cookies()) != 0
    open_session.find_element(By.CSS_SELECTOR, "#react-burger-menu-btn").click()
    time.sleep(1)
    open_session.find_element(By.CSS_SELECTOR, "#logout_sidebar_link").click()
    assert len(open_session.get_cookies()) == 0
