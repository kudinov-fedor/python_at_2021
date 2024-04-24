import pytest
from selenium.common import NoAlertPresentException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("open_tool_tips")
def test_tooltip_for_button(session):
    button = session.find_element(By.CSS_SELECTOR, "button.btn-success#toolTipButton")
    AC(session).move_to_element(button).perform()
    Wait(session, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#buttonToolTip")))
    tooltip = session.find_element(By.CSS_SELECTOR, "#buttonToolTip")
    assert tooltip.text == 'You hovered over the Button'


@pytest.mark.usefixtures("open_progress_bar")
def test_progress_bar(session):
    session.find_element(By.CSS_SELECTOR, "button#startStopButton").click()
    Wait(session, 11).until(EC.text_to_be_present_in_element((By.XPATH, "//*[@id='progressBar']/div"), '100%'))
    progress_bar = session.find_element(By.XPATH, "//*[@id='progressBar']/div")
    assert progress_bar.text == '100%'


@pytest.mark.usefixtures("open_alerts")
def test_alert(session):
    session.find_element(By.CSS_SELECTOR, "button#alertButton").click()
    alert = session.switch_to.alert
    assert alert
    alert.accept()
    with pytest.raises(NoAlertPresentException):
        alert.accept()
        raise AssertionError


@pytest.mark.usefixtures("open_frames")
def test_text_in_frames(session):
    session.switch_to.frame('frame1')
    frame = session.find_element(By.CSS_SELECTOR, "h1#sampleHeading")
    assert frame.text == 'This is a sample page'
    session.switch_to.parent_frame()
    session.switch_to.frame('frame2')
    frame = session.find_element(By.XPATH, "//*[@id='sampleHeading']")
    assert frame.text == 'This is a sample page'
    session.switch_to.parent_frame()
    with pytest.raises(NoSuchElementException):
        session.find_element(By.XPATH, "//*[@id='sampleHeading']")
        raise AssertionError
