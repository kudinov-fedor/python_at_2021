import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


HOST = "https://www.saucedemo.com"
LOGIN = "standard_user"
PASSWORD = "secret_sauce"


@pytest.fixture(scope="function", autouse=True)
def session():
    session = Chrome()
    yield session
    session.quit()


@pytest.fixture(autouse=True)
def login(session):
    session.get(HOST)

    session.find_element(By.ID, "user-name").send_keys(LOGIN)
    session.find_element(By.ID, "password").send_keys(PASSWORD)
    session.find_element(By.ID, "login-button").click()


@pytest.fixture
@pytest.mark.usefixture("login")
def three_items_in_the_cart(session):
    element = session.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
    assert len(element) == 6

    element[0].find_element(By.XPATH, ".//*[@class='pricebar']//button").click()
    element[3].find_element(By.XPATH, ".//*[@class='pricebar']//button").click()
    element[5].find_element(By.XPATH, ".//*[@class='pricebar']//button").click()
