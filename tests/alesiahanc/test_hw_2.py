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


def clickSubmit(session):
    el = session.find_element(By.CSS_SELECTOR, "#submit")
    el.location_once_scrolled_into_view
    return el.click()


def test_validate_email(session):
    session.get("https://demoqa.com/text-box")
    session.find_element(By.CSS_SELECTOR, "#userEmail").send_keys("some@gmail.com")

    clickSubmit(session)

    val = session.find_element(By.CSS_SELECTOR, "#email").text
    assert val == 'Email:some@gmail.com'


testdata = [
    ("test1", "test1"),
    ("213,.~", "213,.~"),
    ("тест", "тест")
]


@pytest.mark.parametrize("text_input, expected", testdata)
def test_validate_fullname(text_input, expected, session):
    session.get("https://demoqa.com/text-box")
    session.find_element(By.CSS_SELECTOR, "#userName").send_keys(text_input)

    clickSubmit(session)

    val = session.find_element(By.CSS_SELECTOR, "#name").text
    assert val == "Name:"+expected


def test_validate_email(session):
    session.get("https://demoqa.com/text-box")
    session.find_element(By.CSS_SELECTOR, "#currentAddress").send_keys("some")

    clickSubmit(session)

    val = session.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[6]/div/p").text
    assert val == 'Current Address :some'


def test_validate_checkbox(session):
    session.get("https://demoqa.com/checkbox")
    checkbox = session.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/ol/li/span/label/span[3]")
    checkbox.click()
    val = session.find_element(By.CSS_SELECTOR, "#result > span:nth-child(2)").text
    assert val == "home"


def test_validate_rb(session):
    session.get("https://demoqa.com/radio-button")
    # for some reasons search by id doesn't work; wondering why:
    # radiobutton = session.find_element(By.ID, "yesRadio")
    # radiobutton.click()
    session.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/label").click()
    val = session.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p").text
    assert val == "You have selected Yes"


def test_validate_no_rb(session):
    session.get("https://demoqa.com/radio-button")
    nobtn = session.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[4]/label")
    href_data = nobtn.get_attribute('href')
    assert href_data == None


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
    session.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button").click()
    val = session.find_element(By.CSS_SELECTOR, "#dynamicClickMessage").text
    assert val == "You have done a dynamic click"

