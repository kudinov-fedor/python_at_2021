import pytest
from typing import List
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

HOST = "https://www.saucedemo.com"
LOGIN = "standard_user"
PASSWORD = "secret_sauce"


def wait_and_click(session, by, locator):
    WebDriverWait(session, 5).until(EC.element_to_be_clickable((by, locator))).click()


def wait_until_all_elements_visible(session, by, locator) -> List[WebElement]:
    return WebDriverWait(session, 5).until(EC.visibility_of_all_elements_located((by, locator)))


@pytest.fixture(scope="function")
def session():
    driver = Chrome()
    driver.get(HOST)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login(session):
    session.find_element(By.ID, "user-name").send_keys(LOGIN)
    session.find_element(By.ID, "password").send_keys(PASSWORD)
    wait_and_click(session, By.ID, "login-button")


@pytest.mark.usefixtures("login")
def test_add_products_to_cart_and_checkout(session):
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
    items = session.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
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


@pytest.mark.usefixtures("login")
def test_menu_items(session):
    """ перевірити кількість і назви menu items
    1 - клікнути по burger menu button
    2 - перевірити кількість items
    3 - перевірити порядок найменувань items
    """

    # перейти у меню
    wait_and_click(session, By.ID, "react-burger-menu-btn")

    # перевірити кількість items меню
    menu_items = wait_until_all_elements_visible(session, By.CSS_SELECTOR, ".bm-menu a[id]")
    assert len(menu_items) == 4

    # перевірити порядок найменувань items меню
    expected_menu_links_texts = ["All Items", "About", "Logout", "Reset App State"]
    actual_menu_links_texts = [item.text for item in menu_items]
    assert actual_menu_links_texts == expected_menu_links_texts, f"Expected menu item texts do not match"


@pytest.mark.usefixtures("login")
def test_prices_in_ascending_order(session):
    """перевірити сортування в порядку зростанння
    1 - клікнути по dropdown сортування
    2 - клікнути Price (low to high)
    3 - перевірити, що ціни на картках з товарами йдуть у зростаючому порядку
    """

    # налаштувати сортування у порядку зростання
    wait_and_click(session, By.CSS_SELECTOR, "select[data-test='product-sort-container']")
    wait_and_click(session, By.XPATH, "//option[text()='Price (low to high)']")

    price_elements = wait_until_all_elements_visible(session, By.CSS_SELECTOR, "div[data-test='inventory-item-price']")

    # прибрати знак долара та конвернути значення цін до float
    prices_values = [float(price_element.text.replace('$', '')) for price_element in price_elements]

    # перевірити поточні ціни відсортованні в порядку зростання
    assert prices_values == sorted(prices_values), f"Prices are not in the ascending order: {prices_values}"