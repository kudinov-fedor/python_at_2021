
from selenium.webdriver.common.by import By
from tests.threc.HW4_selectable.conftest import HOST


def test_radio(driver):
    driver.get(HOST + '/radio-button')

    driver.find_element(By.XPATH, "//label[@for='yesRadio']").click()
    text = driver.find_element(By.CSS_SELECTOR, ".text-success").text
    assert text == 'Yes'

    driver.find_element(By.XPATH, "//label[@for='impressiveRadio']").click()
    text = driver.find_element(By.CSS_SELECTOR, ".text-success").text
    assert text == 'Impressive'

    driver.find_element(By.XPATH, "//label[@for='noRadio']").click()
    text = driver.find_element(By.CSS_SELECTOR, ".text-success").text
    assert text == 'Impressive'
