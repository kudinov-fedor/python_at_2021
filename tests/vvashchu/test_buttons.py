from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC


DEMOQA_HOST = 'https://demoqa.com/'


def test_double_click(driver):
    driver.get(DEMOQA_HOST + "buttons")
    double_click = driver.find_element(By.CSS_SELECTOR, "#doubleClickBtn")
    AC(driver).double_click(double_click).perform()
    text = driver.find_element(By.CSS_SELECTOR, "#doubleClickMessage").text
    assert text == 'You have done a double click'


def test_right_click(driver):
    driver.get(DEMOQA_HOST + "buttons")
    right_click = driver.find_element(By.CSS_SELECTOR, "#rightClickBtn")
    AC(driver).context_click(right_click).perform()
    text = driver.find_element(By.CSS_SELECTOR, "#rightClickMessage").text
    assert text == 'You have done a right click'


def test_click_me(driver):
    driver.get(DEMOQA_HOST + "buttons")
    click_me = driver.find_element(By.XPATH, "//button[text()='Click Me']")
    AC(driver).click(click_me).perform()
    text = driver.find_element(By.CSS_SELECTOR, "#dynamicClickMessage").text
    assert text == 'You have done a dynamic click'
