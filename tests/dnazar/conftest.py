import pytest
from selenium.webdriver import Chrome, ChromeOptions


@pytest.fixture
def session():
    options = ChromeOptions()
    session = Chrome(options=options)
    session.maximize_window()
    yield session
    session.quit()
