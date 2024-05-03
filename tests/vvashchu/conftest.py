import pytest
from selenium.webdriver import Chrome, ChromeOptions
from tests.vvashchu.locators import LoginPage
from tests.vvashchu.locators import ProductPage

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
    session.find_element(*LoginPage.UserName).send_keys(LOGIN)
    session.find_element(*LoginPage.Password).send_keys(PASSORD)
    session.find_element(*LoginPage.LoginBtn).click()


@pytest.fixture
@pytest.mark.usefixtures("login")
def cart_with_2_items(session):

    cart_items = session.find_elements(*ProductPage.product)
    assert len(cart_items) == 6

    cart_items[0].find_element(*ProductPage.product_add_to_cart_btn).click()
    cart_items[2].find_element(*ProductPage.product_add_to_cart_btn).click()
