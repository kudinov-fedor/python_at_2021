import os
import pytest
from selenium.webdriver import Chrome, Firefox, Edge, Safari, ChromeOptions, Remote
from selenium.webdriver.common.by import By


@pytest.fixture
def session():

    options = ChromeOptions()

    # allow camera
    prefs = {"profile.managed_default_content_settings.media_stream": 1}
    options.add_experimental_option("prefs", prefs)

    session = Chrome(options=options)
    session.maximize_window()
    yield session
    session.quit()


def test_cam(session):
    session.get("https://webcamtoy.com/")
    session.find_element(By.ID, "button-init").click()

    # remove ads
    script = """
    els = $(arguments[0])
    for (i = 0; i < els.length; i++){els[i].style.display = "none";}
    """
    session.execute_script(script, "ins.adsbygoogle")

    import time
    time.sleep(5)  # todo replace by Explicit wait

    session.find_element(By.ID, "button-capture").click()
