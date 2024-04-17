import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

HOST = "https://www.saucedemo.com"
LOGIN = "standard_user"
PASSORD = "secret_sauce"


@pytest.fixture
def session():
    config = ChromeOptions()
    config.add_argument("--incognito")
    session = Chrome(options=config)
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
def test_basic(session):
    """
    check the cart indicator
    go to the cart
    check number of products in the cart
    go to checkout
    fill the form
    check if the cart is empty after order submission
    """

    # перевірка індикатора корзини
    cart = session.find_element(By.ID, "shopping_cart_container")
    cart_badge = cart.find_element(By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
    assert cart_badge.text == '2'

    # перехід в корзину
    cart.click()

    # перевірка кількості елементів в корзині
    items = session.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
    assert len(items) == 2

    # перехід до оформлення замовлення
    session.find_element(By.ID, "checkout").click()

    # заповнення форми замовлення
    session.find_element(By.ID, "first-name").send_keys("Lilia")
    session.find_element(By.ID, "last-name").send_keys("Broks")
    session.find_element(By.ID, "postal-code").send_keys("001011")
    session.find_element(By.ID, "continue").click()

    # виконання замовлення
    session.find_element(By.ID, "finish").click()

    # перевірка, що корзина пуста
    session.find_element(By.ID, "back-to-products").click()
    cart = session.find_element(By.ID, "shopping_cart_container")

    with pytest.raises(NoSuchElementException):
        cart.find_element(By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")


@pytest.mark.usefixtures("cart_with_2_items")
def test_product_can_be_removed(session):
    """
    check the cart indicator
    go to the cart
    check the number of products in the cart
    delete one product
    check the number of products in cart
    """

    # перевірка індикатора корзини
    cart = session.find_element(By.ID, "shopping_cart_container")
    cart_badge = cart.find_element(By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
    assert cart_badge.text == '2'

    # перехід в корзину
    cart.click()

    # перевірка кількості елементів в корзині
    items = session.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
    assert len(items) == 2

    # видалення елементу
    items[0].find_element(By.CSS_SELECTOR, "button#remove-sauce-labs-backpack").click()

    # перевірка кількості елементів в корзині
    items = session.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
    assert len(items) == 1


def test_checkout_disabled_if_cart_empty(session):
    """
    go to the cart
    check if checkout is disabled
    """

    # перехід в корзину
    cart = session.find_element(By.ID, "shopping_cart_container")
    cart.click()

    # перевірка кількості елементів в корзині
    items = session.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
    assert len(items) == 0

    checkout_button = session.find_element(By.CSS_SELECTOR, "#checkout").is_enabled()
    assert checkout_button is False
