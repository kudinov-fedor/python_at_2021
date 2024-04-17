import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from selenium.common import NoSuchElementException

HOST = "https://www.saucedemo.com"
LOGIN = "standard_user"
PASSWORD = "secret_sauce"
START_PAGE = "https://www.saucedemo.com/inventory.html"


@pytest.fixture
def driver():
    session = Chrome()
    session.implicitly_wait(0.5)
    yield session
    session.quit()


@pytest.fixture(autouse=True)
def login_to_system(driver):
    driver.get(HOST)
    driver.find_element(By.ID, "user-name").send_keys(LOGIN)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()


@pytest.fixture
@pytest.mark.usefixtures("login_to_system")
def add_to_cart(driver):
    elements = driver.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
    elements[0].find_element(By.XPATH, ".//*[@class='pricebar']//button").click()
    elements[1].find_element(By.XPATH, ".//*[@class='pricebar']//button").click()
    elements[2].find_element(By.XPATH, ".//*[@class='pricebar']//button").click()
    cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_container")
    cart_link.click()


def test_start_page(driver):
    """check START PAGE"""
    current_page = driver.current_url
    assert current_page == START_PAGE


def test_elements(driver):
    """check items on page"""
    elements = driver.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
    assert len(elements) == 6


@pytest.mark.usefixtures("add_to_cart")
def test_delete_all_from_cart(driver):
    """check that basket is empty"""
    items = driver.find_elements(By.CLASS_NAME, "cart_item")
    items[0].find_element(By.CSS_SELECTOR, "button#remove-sauce-labs-backpack").click()
    items[1].find_element(By.CSS_SELECTOR, "button#remove-sauce-labs-bike-light").click()
    items[2].find_element(By.CSS_SELECTOR, "button#remove-sauce-labs-bolt-t-shirt").click()

    cart = driver.find_element(By.ID, "shopping_cart_container")
    with pytest.raises(NoSuchElementException):
        cart.find_element(By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")

    assert driver.current_url == "https://www.saucedemo.com/cart.html"
