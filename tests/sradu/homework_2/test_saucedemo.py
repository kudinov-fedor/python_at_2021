import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


HOST = "https://www.saucedemo.com"
LOGIN = "standard_user"
PASSWORD = "secret_sauce"


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


""" перевірити кількість і назви menu items
1 - клікнути по burger menu button
2 - перевірити кількість items
3 - перевірити порядок найменувань items
"""


def test_menu_items(session, login):
    WebDriverWait(session, 10).until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))).click()
    WebDriverWait(session, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".bm-menu a[id]")))
    size = len(session.find_elements(By.CSS_SELECTOR, ".bm-menu a[id]"))
    assert size == 4

    actual_menu_links = session.find_elements(By.CSS_SELECTOR, ".bm-menu a[id]")
    expected_menu_links_texts = ["All Items", "About", "Logout", "Reset App State"]
    assert len(actual_menu_links) == 4, f"Expected 4 menu items, but found {len(actual_menu_links)}"

    for actual_link, expected_link_text in zip(actual_menu_links, expected_menu_links_texts):
        assert actual_link.text == expected_link_text, f"Expected '{expected_link_text}', but got '{actual_link.text}'"


"""перевірити сортування в порядку зростанння
1 - клікнути по dropdown сортування
2 - клікнути Price (low to high) 
3 - перевірити, що ціни на картках з товарами йдуть у зростаючому порядку
"""


def test_prices_in_ascending_order(session, login):
    WebDriverWait(session, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "select[data-test='product-sort-container']"))
    ).click()

    WebDriverWait(session, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//option[text()='Price (low to high)']"))
    ).click()

    WebDriverWait(session, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div[data-test='inventory-item-price']")))

    price_elements = session.find_elements(By.CSS_SELECTOR, "div[data-test='inventory-item-price']")
    prices_values = [float(price_element.text.replace('$', '')) for price_element in price_elements]

    print(f"Expected prices: {prices_values}")
    assert prices_values == sorted(prices_values), f"Prices are not in the ascending order: {prices_values}"

