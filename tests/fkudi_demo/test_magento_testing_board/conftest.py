import pytest

from selenium.webdriver import Chrome

from magento_softwaretesting_board import config


@pytest.fixture
def user():
    return {"login": config.LOGIN,
            "password": config.PASSWORD,
            "name": config.USER_NAME}


@pytest.fixture
def session():
    session = Chrome()

    with session:
        session.maximize_window()
        yield session
