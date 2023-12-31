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
        yield session


def click_submit(session):
    el = session.find_element(By.CSS_SELECTOR, "#submit")
    el.location_once_scrolled_into_view
    return el.click()


def test_validate_email(session):
    session.get("https://demoqa.com/text-box")
    session.find_element(By.CSS_SELECTOR, "#userEmail").send_keys("some@gmail.com")

    click_submit(session)

    val = session.find_element(By.CSS_SELECTOR, "#email").text
    assert val == 'Email:some@gmail.com'


@pytest.mark.parametrize("text_input, expected", [
    ("test1", "test1"),
    ("213,.~", "213,.~"),
    ("тест", "тест")
])
def test_validate_fullname(text_input, expected, session):
    session.get("https://demoqa.com/text-box")
    session.find_element(By.CSS_SELECTOR, "#userName").send_keys(text_input)

    click_submit(session)

    val = session.find_element(By.CSS_SELECTOR, "#name").text
    assert val == "Name:" + expected


def test_validate_email(session):
    session.get("https://demoqa.com/text-box")
    session.find_element(By.CSS_SELECTOR, "#currentAddress").send_keys("some")

    click_submit(session)

    val = session.find_element(By.XPATH, "//p[@id='currentAddress']").text
    assert val == 'Current Address :some'


def test_validate_checkbox(session):
    session.get("https://demoqa.com/checkbox")
    checkbox = session.find_element(By.XPATH, "//*[@class='rct-title']")
    checkbox.click()
    val = session.find_element(By.CSS_SELECTOR, "#result > span:nth-child(2)").text
    assert val == "home"


def test_validate_rb(session):
    session.get("https://demoqa.com/radio-button")
    session.find_element(By.XPATH, "//*[contains(@class, 'custom-control')][contains(@class, 'custom-radio')][contains(@class, 'custom-control-inline')]").click()
    val = session.find_element(By.XPATH, "//*[@class='mt-3']").text
    assert val == "You have selected Yes"


def test_validate_no_rb(session):
    session.get("https://demoqa.com/radio-button")
    is_btn_enabled = session.find_element(By.XPATH, "//*[@class='custom-control-input disabled']").is_enabled()
    assert is_btn_enabled == False


def test_double_click(session):
    session.get("https://demoqa.com/buttons")
    btn = session.find_element(By.ID, "doubleClickBtn")
    action = AC(session)
    action.double_click(btn).perform()
    val = session.find_element(By.CSS_SELECTOR, "#doubleClickMessage").text
    assert val == "You have done a double click"


def test_right_mouse_click(session):
    session.get("https://demoqa.com/buttons")
    btn = session.find_element(By.ID, "rightClickBtn")
    action = AC(session)
    action.context_click(btn).perform()
    val = session.find_element(By.CSS_SELECTOR, "#rightClickMessage").text
    assert val == "You have done a right click"


def test_button_click(session):
    session.get("https://demoqa.com/buttons")
    session.find_element(By.XPATH, "//button[text()='Click Me']").click()
    val = session.find_element(By.CSS_SELECTOR, "#dynamicClickMessage").text
    assert val == "You have done a dynamic click"
