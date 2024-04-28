import pytest
from selenium.webdriver import Chrome


HOST = "https://demoqa.com"


@pytest.fixture(scope="function")
def session():
    my_session = Chrome()
    my_session.implicitly_wait(1)
    yield my_session

    # tear down
    my_session.quit()
