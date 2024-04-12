import pytest
from selenium.webdriver import Chrome
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

HOST = "https://www.saucedemo.com"
LOGIN = "standard_user"
PASSORD = "secret_sauce"


@pytest.fixture
def session():
    session = Chrome()
    yield session
    session.quit()


@pytest.fixture(autouse=True)
def login(session):
    session.get(HOST)

    # вхід в систему
    session.find_element(By.ID, "user-name").send_keys(LOGIN)
    session.find_element(By.ID, "password").send_keys(PASSORD)
    session.find_element(By.ID, "login-button").click()


@pytest.fixture
@pytest.mark.usefixtures("login")
def cart_with_2_items(session):
    elements = session.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
    assert len(elements) == 6

    elements[0].find_element(By.XPATH, ".//*[@class='pricebar']//button").click()

    elements[2].find_element(By.XPATH, ".//*[@class='pricebar']//button").click()


@pytest.mark.usefixtures("cart_with_2_items")
def test_basic_flow(session):
    """
    check number of products on the page
    add 2 products to the cart
    check cart indicator
    go to cart
    check number of products in cart
    go to checkout
    fill the form
    check that cart is empty after order submission
    """

    # перевірити індикатор корзини
    cart = session.find_element(By.ID, "shopping_cart_container")
    cart_badge = cart.find_element(By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
    assert cart_badge.text == '2'

    # перейти в корзину
    cart.click()

    # перевірити кількість елементів в корзині
    items = session.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
    assert len(items) == 2

    # перейти до оформлення замовлення
    session.find_element(By.ID, "checkout").click()

    # заповнення форми замовлення
    session.find_element(By.ID, "first-name").send_keys("Jonh")
    session.find_element(By.ID, "last-name").send_keys("Adams")
    session.find_element(By.ID, "postal-code").send_keys("001011")
    session.find_element(By.ID, "continue").click()

    # виконати замовлення
    session.find_element(By.ID, "finish").click()

    # перевірити, що корзина пуста
    session.find_element(By.ID, "back-to-products").click()
    cart = session.find_element(By.ID, "shopping_cart_container")

    with pytest.raises(NoSuchElementException):
        cart.find_element(By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")


@pytest.mark.usefixtures("cart_with_2_items")
def test_product_can_be_removed_flow(session):
    """
    check number of products on the page
    add 2 products to the cart
    go to cart
    check number of products in cart
    delete one product
    check number of products in cart
    """

    # перевірити індикатор корзини
    cart = session.find_element(By.ID, "shopping_cart_container")
    cart_badge = cart.find_element(By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
    assert cart_badge.text == '2'

    # перейти в корзину
    cart.click()

    # перевірити кількість елементів в корзині
    items = session.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
    assert len(items) == 2

    # delete element
    items[0].find_element(By.CSS_SELECTOR, "button#remove-sauce-labs-backpack").click()

    # перевірити кількість елементів в корзині
    items = session.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
    assert len(items) == 1


def test_cart_is_empty_after_login(session):
    """
    login
    go to cart
    check number cart is empty
    """

    # перейти в корзину
    cart = session.find_element(By.ID, "shopping_cart_container")
    cart.click()

    # перевірити кількість елементів в корзині
    items = session.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
    assert len(items) == 0


def test_checkout_disabled_if_cart_empty(session):
    """
    login
    go to cart
    check checkout is disabled
    """

    # перейти в корзину
    cart = session.find_element(By.ID, "shopping_cart_container")
    cart.click()

    # перевірити кількість елементів в корзині
    items = session.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
    assert len(items) == 0

    checkout_button=session.find_element(By.CSS_SELECTOR, "#checkout").is_enabled()
    assert checkout_button == False

    