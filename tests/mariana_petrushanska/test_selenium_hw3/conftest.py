import pytest
from selenium.webdriver import Chrome
from tests.mariana_petrushanska.test_selenium_hw3 import constants


@pytest.fixture(scope="function")
def session():
    session = Chrome()
    session.implicitly_wait(0.5)
    yield session
    session.quit()


@pytest.fixture
def open_dynamic_properties_page(session):
    session.get(constants.HOST + "/dynamic-properties")


@pytest.fixture
def open_buttons_page(session):
    session.get(constants.HOST + "/buttons")
