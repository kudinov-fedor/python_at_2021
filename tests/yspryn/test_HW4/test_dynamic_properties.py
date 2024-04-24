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
    button_color_on_the_begin = (session.find_element(By.XPATH, "//button[@id='colorChange']")
                                 .value_of_css_property('color'))
    print(f'begin = {button_color_on_the_begin}')
    # Wait(session, 6).until(EC.presence_of_element_located((By.XPATH, "//button[@id='colorChange']"
    #                                                              "[contains(@class,'text-danger')]")))
    import time
    time.sleep(10)
    button_color_changed = session.find_element(By.XPATH, "//button[@id='colorChange']"
                                            "[contains(@class,'text-danger')]").value_of_css_property('color')
    print(f'end = {button_color_changed}')

    assert button_color_on_the_begin != button_color_changed

