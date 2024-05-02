import pytest
from selenium.webdriver import Chrome


HOST = "https://demoqa.com/"


@pytest.fixture(scope="function")
def session():
    session = Chrome()
    session.implicitly_wait(5)
    yield session
    session.quit()
