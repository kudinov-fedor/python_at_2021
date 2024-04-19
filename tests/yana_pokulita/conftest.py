import pytest
from selenium.webdriver import Chrome
from tests.yana_pokulita.locators import LoginPage
from tests.yana_pokulita.locators import ProductPage


HOST = "https://www.saucedemo.com"
LOGIN = "standard_user"
PASSORD = "secret_sauce"


@pytest.fixture
def session():
    session = Chrome()
    yield session
    session.quit()


@pytest.fixture(autouse=True)
def login(session):
    session.get(HOST)

    # enter to the system
    session.find_element(*LoginPage.UserName).send_keys(LOGIN)
    session.find_element(*LoginPage.Password).send_keys(PASSORD)
    session.find_element(*LoginPage.LoginBtn).click()


@pytest.fixture
@pytest.mark.usefixtures("login")
def cart_with_2_items(session):
    # (By.XPATH, "//*[@id='inventory_container']/*")
    elements = session.find_elements(*ProductPage.Elements)
    assert len(elements) == 6

    # (By.CSS_SELECTOR, ".pricebar .btn_inventory ")
    elements[0].find_element(*ProductPage.Element).click()
    # By.CSS_SELECTOR, ".pricebar .btn_inventory "
    elements[2].find_element(*ProductPage.Element).click()
