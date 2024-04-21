import pytest
from selenium.webdriver.common.by import By

HOST = 'https://demoqa.com'


@pytest.mark.usefixture("driver")
def test_radio(driver):
    driver.get(HOST + '/radio-button')

    driver.find_element(By.XPATH, "//label[@for='yesRadio']").click()
    text = driver.find_element(By.XPATH, "//*[@id='app']/div/div/div/div[2]/div[2]/p/span").text
    assert text == 'Yes'

    driver.find_element(By.XPATH, "//label[@for='impressiveRadio']").click()
    text = driver.find_element(By.XPATH, "//*[@id='app']/div/div/div/div[2]/div[2]/p/span").text
    assert text == 'Impressive'

    driver.find_element(By.XPATH, "//label[@for='noRadio']").click()
    text = driver.find_element(By.XPATH, "//*[@id='app']/div/div/div/div[2]/div[2]/p/span").text
    assert text == 'Impressive'

    driver.close()
