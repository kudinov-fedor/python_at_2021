from selenium.webdriver import Chrome
import pytest

HOST = 'https://demoqa.com'


@pytest.fixture()
def driver():
    driver = Chrome()
    driver.implicitly_wait(3)

    yield driver

    # tear down
    driver.quit()
