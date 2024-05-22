import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.webdriver import WebDriver
from tests.ysemenov.hw6.pages import LoginPage, InventoryPage
from tests.ysemenov.hw6.constants import LOGIN, PASSWORD


@pytest.fixture(scope="function")
def session():
    session = Chrome()
    yield session

    # tear down
    session.quit()


@pytest.fixture(autouse=True)
def landing_page(session: WebDriver) -> InventoryPage:
    login_page = LoginPage(session)
    landing_page = login_page.open() \
        .log_in(LOGIN, PASSWORD)
    return landing_page
