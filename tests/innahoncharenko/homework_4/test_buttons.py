import pytest
from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait

from selenium.webdriver.common.action_chains import ActionChains as AC

URL = "https://demoqa.com/buttons"


@pytest.fixture
def open_session():
    session = Chrome()

    session.get(URL)

    yield session

    session.quit()


def test_double_click_button(open_session):
    double_click_button = open_session.find_element(By.ID, "doubleClickBtn")
    double_click_button_result_locator = (By.ID, "doubleClickMessage")

    AC(open_session).double_click(double_click_button).perform()

    result = Wait(open_session, 1).until(EC.presence_of_element_located(double_click_button_result_locator))

    assert "You have done a double click" == result.text


def test_right_click_button(open_session):
    right_click_button = open_session.find_element(By.ID, "rightClickBtn")
    right_click_button_result_locator = (By.ID,"rightClickMessage")

    AC(open_session).context_click(right_click_button).perform()
    result = Wait(open_session, 1).until(EC.presence_of_element_located(right_click_button_result_locator))

    assert "You have done a right click" == result.text


def test_click_me_button(open_session):
    click_me_button = open_session.find_element(By.XPATH, "//button[text()='Click Me']")
    click_me_button_result_locator = (By.ID, "dynamicClickMessage")

    AC(open_session).click(click_me_button).perform()
    result = Wait(open_session, 1).until(EC.presence_of_element_located(click_me_button_result_locator))

    assert "You have done a dynamic click" == result.text

