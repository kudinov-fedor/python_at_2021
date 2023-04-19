import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def test_setup():
    global driver
    driver = Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/text-box")
    yield
    driver.close()
    driver.quit()


def test_text_box():
    full_name = driver.find_element(By.XPATH, "//input[@id='userName']")
    email = driver.find_element(By.XPATH,"//input[@id='userEmail']")
    current_address = driver.find_element(By.CSS_SELECTOR, "textarea#currentAddress")
    permanent_address = driver.find_element(By.CSS_SELECTOR, "textarea#permanentAddress")
    btn_submit = driver.find_element(By.CSS_SELECTOR, "button#submit")

    full_name.send_keys("Johnny Bravo")
    email.send_keys("johnny@bravo.com")
    current_address.send_keys("Aron City")
    permanent_address.send_keys("USA")
    btn_submit.click()

    processed_name = driver.find_element(By.CSS_SELECTOR, "p#name")
    processed_email = driver.find_element(By.CSS_SELECTOR, "p#email")
    processed_current_address = driver.find_element(By.CSS_SELECTOR, "p#currentAddress")
    processed_permanent_address = driver.find_element(By.CSS_SELECTOR, "p#permanentAddress")

    assert processed_name.text == "Name:Johnny Bravo"
    assert processed_email.text == "Email:johnny@bravo.com"
    assert processed_current_address.text == "Current Address :Aron City"
    assert processed_permanent_address.text == "Permananet Address :USA"
