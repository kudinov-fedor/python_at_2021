import pytest
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


# Constants
HOST = "https://www.saucedemo.com"
LOGIN = "standard_user"
PASSWORD = "secret_sauce"


# Fixture for Chrome browser
@pytest.fixture(scope="function")
def session():
    session = Chrome()
    session.get(HOST)
    yield session
    session.quit()


@pytest.fixture(scope="function")
def login(session):
    session.find_element(By.ID, "user-name").send_keys(LOGIN)
    session.find_element(By.ID, "password").send_keys(PASSWORD)
    session.find_element(By.ID, "login-button").click()
    return session


def test_add_products_to_cart_and_checkout(session, login):
    elements = session.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
    assert len(elements) == 6, "Expected 6 inventory items"

    # додати перший продукт в корзину
    elements[0].find_element(By.XPATH, ".//*[@class='pricebar']//button").click()
    # додати третій продукт в корзину
    elements[2].find_element(By.XPATH, ".//*[@class='pricebar']//button").click()

    # перевірити індикатор корзини
    cart_badge = session.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == '2', "Expected 2 items in the cart"

    # перейти в корзину
    session.find_element(By.ID, "shopping_cart_container").click()

    # перевірити кількість елементів в корзині
    items = login.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
    assert len(items) == 2, "Expected 2 items in the cart checkout"

    # перейти до оформлення замовлення
    session.find_element(By.ID, "checkout").click()
    session.find_element(By.ID, "first-name").send_keys("Jonh")
    session.find_element(By.ID, "last-name").send_keys("Adams")
    session.find_element(By.ID, "postal-code").send_keys("001011")
    session.find_element(By.ID, "continue").click()

    # виконати замовлення
    session.find_element(By.ID, "finish").click()
    session.find_element(By.ID, "back-to-products").click()

    # перевірити, що корзина пуста
    cart = session.find_element(By.ID, "shopping_cart_container")
    with pytest.raises(NoSuchElementException):
        cart.find_element(By.CLASS_NAME, "shopping_cart_badge")
