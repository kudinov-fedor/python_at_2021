import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from tests.sradu.homework_2.utils import wait_for_element, wait_until_all_elements_visible

HOST = "https://www.saucedemo.com"
LOGIN = "standard_user"
PASSWORD = "secret_sauce"


@pytest.fixture
def session():
    driver = Chrome()
    driver.get(HOST)
    yield driver
    driver.quit()


@pytest.fixture
def login(session):
    session.find_element(By.ID, "user-name").send_keys(LOGIN)
    session.find_element(By.ID, "password").send_keys(PASSWORD)
    wait_for_element(session, By.ID, "login-button").click()


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
    wait_for_element(session, By.ID, "react-burger-menu-btn").click()

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
    wait_for_element(session, By.CSS_SELECTOR, "select[data-test='product-sort-container']").click()
    wait_for_element(session, By.XPATH, "//option[text()='Price (low to high)']").click()

    price_elements = wait_until_all_elements_visible(session, By.CSS_SELECTOR, "div[data-test='inventory-item-price']")

    # прибрати знак долара та конвернути значення цін до float
    prices_values = [float(price_element.text.replace('$', '')) for price_element in price_elements]

    # перевірити поточні ціни відсортованні в порядку зростання
    assert prices_values == sorted(prices_values), f"Prices are not in the ascending order: {prices_values}"
