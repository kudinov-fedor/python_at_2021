import pytest

from selenium.webdriver import Chrome  # noqa: F401
from selenium.webdriver.remote.webdriver import WebDriver  # noqa: F401
from selenium.webdriver.remote.webelement import WebElement  # noqa: F401
from selenium.webdriver.common.action_chains import ActionChains as AC  # noqa: F401
from selenium.webdriver.common.by import By  # noqa: F401
from selenium.webdriver.common.keys import Keys  # noqa: F401
from selenium.webdriver.support.ui import WebDriverWait as Wait  # noqa: F401
from selenium.webdriver.support import expected_conditions as EC  # noqa: F401
from selenium.common.exceptions import TimeoutException  # noqa: F401


@pytest.fixture
def session():
    session = Chrome()
    # session.implicitly_wait(0.5)

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


def test_ajax(session):
    session.get("https://www.w3schools.com/js/js_ajax_intro.asp")

    btn = session.find_element(By.CSS_SELECTOR, "#demo button")
    btn.click()

    print(session.page_source)

    # import time
    # time.sleep(1)

    # explicit wait
    text = Wait(session, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#demo h1")))

    # text = session.find_element(By.CSS_SELECTOR, "#demo h1")
    assert text.text == "AJAX"
