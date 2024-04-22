import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


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
    session.find_element(By.ID, "user-name").send_keys(LOGIN)
    session.find_element(By.ID, "password").send_keys(PASSWORD)
    session.find_element(By.ID, "login-button").click()


@pytest.fixture
@pytest.mark.usefixtures("user_login")
def cart_with_2_items(session):
    """
    1. Check the number of available products on the page
    2. Add 2 products to cart
    """

    elements = session.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
    assert len(elements) == 6

    elements[0].find_element(By.XPATH, ".//*[@class='pricebar']//button").click()
    elements[2].find_element(By.XPATH, ".//*[@class='pricebar']//button").click()


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
    cart = session.find_element(By.ID, "shopping_cart_container")
    cart_badge = cart.find_element(By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
    assert cart_badge.text == "2"

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
def test_removing_added_product(session):
    """
    1. Open cart page
    2. Verify the number of items it cart
    3. Remove one product
    4. Verify the number of product added in cart
    """

    # перевірити індикатор корзини
    cart = session.find_element(By.ID, "shopping_cart_container")
    cart_badge = cart.find_element(By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
    assert cart_badge.text == "2"

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


@pytest.fixture
def login_and_go_to_cart(session):

    # перейти в корзину
    cart = session.find_element(By.ID, "shopping_cart_container")
    cart.click()

def test_checkout_disabled_if_cart_empty(session, login_and_go_to_cart):
    """
    Verify that the checkout button is disabled
    """

    # перевірити кількість елементів в корзині
    items = session.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
    assert len(items) == 0

    checkout_button=session.find_element(By.CSS_SELECTOR, "#checkout").is_enabled()
    assert checkout_button == False
