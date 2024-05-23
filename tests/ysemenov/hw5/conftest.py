import pytest
from selenium.webdriver import Chrome

HOST = "https://www.saucedemo.com"
LOGIN = "standard_user"
PASSWORD = "secret_sauce"
FIRSTNAME = "Luke"
LASTNAME = "Skywalker"
POSTALCODE = "90210"
MESSAGE_SUCCESS = "Thank you for your order!"


@pytest.fixture(scope="function")
def session():
    session = Chrome()
    yield session

    # tear down
    session.quit()
