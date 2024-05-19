import pytest
from selenium.webdriver import Chrome
from tests.ysemenov.hw6 import pages
from tests.ysemenov.hw6.constants import LOGIN, PASSWORD


@pytest.fixture(scope="function")
def session():
    session = Chrome()
    yield session

    # tear down
    session.quit()


@pytest.fixture(autouse=True)
def setup(session):
    login_page = pages.LoginPage(session)
    inventory_page = login_page.open() \
        .log_in(LOGIN, PASSWORD)
    return inventory_page
