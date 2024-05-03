import pytest
from selenium.webdriver import Chrome
from tests.threc.HW_saucedemo.locators import LoginPage
import constants


@pytest.fixture()
def session():
    session = Chrome()
    yield session

    # tear down
    session.quit()


@pytest.fixture(autouse=True)
def login(session):
    """
    Log in to the site
    """
    session.get(costants.URL_HOST)
    # session.find_element(By.ID, "user-name").send_keys(LOGIN)
    session.find_element(*LoginPage.login).send_keys(costants.LOGIN)

    # session.find_element(By.ID, "password").send_keys(PASSWORD)
    session.find_element(*LoginPage.password).send_keys(costants.PASSWORD)

    # session.find_element(By.ID, "login-button").click()
    session.find_element(*LoginPage.btnLogin).click()
