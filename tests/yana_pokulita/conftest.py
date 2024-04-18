import pytest
from selenium.webdriver import Chrome
from tests.yana_pokulita.locators import ForConfTest

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
    session.find_element(*ForConfTest.UserName).send_keys(LOGIN)
    session.find_element(*ForConfTest.Password).send_keys(PASSORD)
    session.find_element(*ForConfTest.LoginBtn).click()


@pytest.fixture
@pytest.mark.usefixtures("login")
def cart_with_2_items(session):
    # (By.XPATH, "//*[@id='inventory_container']/*")
    elements = session.find_elements(*ForConfTest.Elements)
    assert len(elements) == 6

    # (By.CSS_SELECTOR, ".pricebar .btn_inventory ")
    elements[0].find_element(*ForConfTest.Element1).click()
    # By.CSS_SELECTOR, ".pricebar .btn_inventory "
    elements[2].find_element(*ForConfTest.Element3).click()
