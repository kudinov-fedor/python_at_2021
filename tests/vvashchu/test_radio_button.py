import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC


DEMOQA_HOST = 'https://demoqa.com/'


@pytest.mark.parametrize("radio_button_id, expected_text", [
    ("yesRadio", "Yes"),
    ("impressiveRadio", "Impressive"),
    ("noRadio", "No")
])
def test_radio_btn(driver, radio_button_id, expected_text):
    driver.get(DEMOQA_HOST + "radio-button")
    radio_btn = driver.find_element(By.CSS_SELECTOR, "#" + radio_button_id)
    AC(driver).click(radio_btn).perform()
    text = driver.find_element(By.CSS_SELECTOR, ".text-success").text
    assert text == expected_text
