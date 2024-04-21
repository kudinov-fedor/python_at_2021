import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC


HOST2 = 'https://demoqa.com/'


@pytest.fixture()
def driver():
    driver = Chrome()
    driver.implicitly_wait(1)
    yield driver
    driver.quit()


@pytest.mark.usefixtures("driver")
def test_radiobutton(driver):
    driver.get(HOST2 + "radio-button")
    yes_radio = driver.find_element(By.CSS_SELECTOR, "#yesRadio")
    AC(driver).click(yes_radio).perform()
    text = driver.find_element(By.CSS_SELECTOR, ".text-success").text
    assert text == 'Yes'

    impressive_radio = driver.find_element(By.CSS_SELECTOR, "#impressiveRadio")
    AC(driver).click(impressive_radio).perform()
    text = driver.find_element(By.CSS_SELECTOR, ".text-success").text
    assert text == 'Impressive'

    no_radio = driver.find_element(By.CSS_SELECTOR, "#noRadio")
    AC(driver).click(no_radio).perform()
    text = driver.find_element(By.CSS_SELECTOR, ".text-success").text
    assert text == 'No'
