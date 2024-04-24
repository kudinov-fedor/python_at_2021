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


@pytest.fixture()
def open_buttons_page(session):
    session.get(HOST + "/buttons")


@pytest.fixture()
def open_dynamic_properties(session):
    session.get(HOST + "/dynamic-properties")
