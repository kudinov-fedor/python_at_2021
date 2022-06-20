import pytest
import os
import time
from selenium import webdriver


driver_path = os.environ.get("DRIVER_PATH", "chromedriver")
#HOST = 'https://demoqa.com'
#URL = "/text-box"


@pytest.fixture(scope="session")
def session():
    session = webdriver.Chrome(driver_path)
    time.sleep(2)
    yield session
    session.quit()
    time.sleep(2)



#     driver = webdriver.Chrome(driver_path)
#     #driver.get(HOST + URL)
#     time.sleep(2)
#     driver.maximize_window()
#
#     yield
#     driver.close()
#     time.sleep(1)
#
# def session():