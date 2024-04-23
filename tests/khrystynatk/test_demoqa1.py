import pytest
from tests.khrystynatk.locators_for_textbox import LandingPage
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

HOST = "https://demoqa.com"
FULL_NAME = "Name"
EMAIL = "testmail@gmail.com"
CURRENT_ADDR = "Current"
PERMANENT_ADDR = "Permanent"


@pytest.fixture
def driver():
    session = Chrome()
    session.implicitly_wait(0.5)
    session.maximize_window()
    yield session
    session.quit()


@pytest.fixture(autouse=True)
def open_page(driver):
    driver.get(HOST + "/text-box")


def test_landing_page(driver):
    assert driver.find_element(*LandingPage.inpt_full).is_displayed()
    assert driver.find_element(*LandingPage.inpt_email).is_displayed()
    assert driver.find_element(*LandingPage.inpt_cur_addr).is_displayed()
    assert driver.find_element(*LandingPage.inpt_perm_addr).is_displayed()
    assert driver.find_element(*LandingPage.sbmt_button).is_displayed()
    assert driver.find_element(*LandingPage.sbmt_button).is_enabled()


def test_output(driver):
    inpt_form = driver.find_element(By.CSS_SELECTOR, "form#userForm")
    driver.execute_script("arguments[0].scrollIntoView();", inpt_form)
    inpt_form.find_element(*LandingPage.inpt_full).send_keys(FULL_NAME)
    inpt_form.find_element(*LandingPage.inpt_email).send_keys(EMAIL)
    inpt_form.find_element(*LandingPage.inpt_cur_addr).send_keys(CURRENT_ADDR)
    inpt_form.find_element(*LandingPage.inpt_perm_addr).send_keys(PERMANENT_ADDR)
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*LandingPage.sbmt_button))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(LandingPage.sbmt_button)).click()
    output_area = driver.find_element(By.CSS_SELECTOR, "div#output.mt-4.row")
    assert output_area.is_displayed()
    assert FULL_NAME in output_area.find_element(By.CSS_SELECTOR, "p#name.mb-1").text
    assert EMAIL in output_area.find_element(By.CSS_SELECTOR, "p#email.mb-1").text
    assert CURRENT_ADDR in output_area.find_element(By.CSS_SELECTOR, "p#currentAddress.mb-1").text
    assert PERMANENT_ADDR in output_area.find_element(By.CSS_SELECTOR, "p#permanentAddress.mb-1").text


def test_space_inpt(driver):
    inpt_form = driver.find_element(By.TAG_NAME, "form")
    output_row = driver.find_element(By.CSS_SELECTOR, "div.mt-2.justify-content-end.row")
    AC(driver).scroll_to_element(output_row).perform()
    inpt_form.find_element(*LandingPage.inpt_full).send_keys(Keys.SPACE)
    inpt_form.find_element(*LandingPage.inpt_email).send_keys(Keys.SPACE)
    inpt_form.find_element(*LandingPage.inpt_cur_addr).send_keys(Keys.SPACE)
    inpt_form.find_element(*LandingPage.inpt_perm_addr).send_keys(Keys.SPACE)
    assert inpt_form.find_element(*LandingPage.inpt_full).text == ""
    assert inpt_form.find_element(*LandingPage.inpt_email).text == ""
    assert inpt_form.find_element(*LandingPage.inpt_cur_addr).text == ""
    assert inpt_form.find_element(*LandingPage.inpt_perm_addr).text == ""
