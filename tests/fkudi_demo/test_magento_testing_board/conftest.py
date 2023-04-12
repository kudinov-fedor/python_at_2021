import pytest

from selenium.webdriver import Chrome


@pytest.fixture
def session():
    session = Chrome()

    with session:
        session.maximize_window()
        yield session
