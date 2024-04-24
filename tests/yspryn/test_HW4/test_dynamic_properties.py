import pytest
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.remote.webdriver import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("open_dynamic_properties")
def test_button_appeared_in_5s(session):
    Wait(session, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#visibleAfter")))
    button = session.find_element(By.CSS_SELECTOR, "#visibleAfter")
    assert button.is_displayed()


@pytest.mark.usefixtures("open_dynamic_properties")
def test_button_become_enabled(session):
    Wait(session, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='enableAfter']")))
    button = session.find_element(By.XPATH, "//button[@id='enableAfter']")
    assert button.is_enabled()


@pytest.mark.usefixtures("open_dynamic_properties")
def test_button_color_changed(session):
    Wait(session, 6).until(EC.presence_of_element_located((By.XPATH, "//button[@id='colorChange']"
                                                                     "[contains(@class,'text-danger')]")))
    button_color_changed = session.find_element(By.XPATH, "//button[@id='colorChange'][contains(@class,'text-danger')]")
    button_class = button_color_changed.get_attribute('class')
    assert 'text-danger' in button_class
