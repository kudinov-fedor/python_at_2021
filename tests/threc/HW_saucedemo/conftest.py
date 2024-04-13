import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
HOST = "https://www.saucedemo.com/"


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
    session.get(HOST)
    session.find_element(By.ID, "user-name").send_keys("standard_user")
    session.find_element(By.ID, "password").send_keys("secret_sauce")
    session.find_element(By.ID, "login-button").click()
