import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


HOST = "https://www.saucedemo.com"
LOGIN = "standard_user"
PASSWORD = "secret_sauce"


@pytest.fixture(scope="function")
def session():
    my_session = Chrome()
    yield my_session

    # tear down
    my_session.quit()


@pytest.fixture(autouse=True)
def user_login(session):
    session.get(HOST)
    session.find_element(By.ID, "user-name").send_keys(LOGIN)
    session.find_element(By.ID, "password").send_keys(PASSWORD)
    session.find_element(By.ID, "login-button").click()


@pytest.fixture()
def add_products_to_cart(session):
    elements = session.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
    elements[0].find_element(By.XPATH, ".//*[@class='pricebar']//button").click()
    elements[2].find_element(By.XPATH, ".//*[@class='pricebar']//button").click()


@pytest.fixture()
def enter_cart(session):
    cart = session.find_element(By.ID, "shopping_cart_container")
    cart.click()
