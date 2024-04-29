from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.remote.webdriver import By
from selenium.webdriver.support import expected_conditions as EC

URL_DYNAMIC_PAGE = "https://demoqa.com/dynamic-properties"


def test_button_appeared_in_5s(session):
    session.get(URL_DYNAMIC_PAGE)
    Wait(session, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#visibleAfter")))
    button = session.find_element(By.CSS_SELECTOR, "#visibleAfter")
    assert button.is_displayed()


def test_button_become_enabled(session):
    session.get(URL_DYNAMIC_PAGE)
    Wait(session, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='enableAfter']")))
    button = session.find_element(By.XPATH, "//button[@id='enableAfter']")
    assert button.is_enabled()


def test_button_color_changed(session):
    session.get(URL_DYNAMIC_PAGE)
    Wait(session, 6).until(EC.presence_of_element_located((By.XPATH, "//button[@id='colorChange']"
                                                                     "[contains(@class,'text-danger')]")))
    button_color_changed = session.find_element(By.ID, 'colorChange')
    button_class = button_color_changed.get_attribute('class')
    assert 'text-danger' in button_class
