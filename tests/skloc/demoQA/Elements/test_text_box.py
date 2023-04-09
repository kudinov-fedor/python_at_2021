import pytest
from selenium.webdriver import Chrome


@pytest.fixture(autouse=True)
def test_setup():
    # driver = Chrome('C:\webdrivers\chromedriver.exe')
    global driver
    driver = Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/text-box")
    yield
    driver.close()
    driver.quit()


def test_text_box():
    full_name = driver.find_element_by_xpath("//input[@id='userName']")
    email = driver.find_element_by_xpath("//input[@id='userEmail']")
    current_address = driver.find_element_by_css_selector("textarea#currentAddress")
    permanent_address = driver.find_element_by_css_selector("textarea#permanentAddress")
    btn_submit = driver.find_element_by_css_selector("button#submit")

    full_name.send_keys("Johnny Bravo")
    email.send_keys("johnny@bravo.com")
    current_address.send_keys("Aron City")
    permanent_address.send_keys("USA")
    btn_submit.click()

    processed_name = driver.find_element_by_css_selector("p#name")
    processed_email = driver.find_element_by_css_selector("p#email")
    processed_current_address = driver.find_element_by_css_selector("p#currentAddress")
    processed_permanent_address = driver.find_element_by_css_selector("p#permanentAddress")

    assert processed_name.text == "Name:Johnny Bravo"
    assert processed_email.text == "Email:johnny@bravo.com"
    assert processed_current_address.text == "Current Address:Aron City"
    assert processed_permanent_address.text == "Permanent Address:USA"