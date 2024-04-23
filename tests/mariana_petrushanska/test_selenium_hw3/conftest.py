import pytest
from selenium.webdriver import Chrome

@pytest.fixture(scope="function")
def session():
    session = Chrome()
    session.implicitly_wait(1)
    yield session
    session.quit()
