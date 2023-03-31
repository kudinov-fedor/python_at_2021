import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@pytest.fixture
def session():
    session = Chrome()

    with session:
        session.maximize_window()
        session.get("https://demoqa.com/text-box")
        yield session


def test_validate_email(session):
    session.find_element(By.CSS_SELECTOR, "#userEmail").send_keys("some@gmail.com")

    el = session.find_element(By.CSS_SELECTOR, "#submit")
    el.click()

    val = session.find_element(By.CSS_SELECTOR, "#email").text
    assert val == 'Email:some@gmail.com'


def test_validate_name(session):
    session.find_element(By.CSS_SELECTOR, "#userEmail").send_keys("some@gmail.com")
    session.find_element(By.CSS_SELECTOR, "#submit").click()
    val = session.find_element(By.CSS_SELECTOR, "#email").text
    assert val == 'Email:some@gmail.com'
