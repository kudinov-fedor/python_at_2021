import pytest
import os
import time
from selenium import webdriver


driver_path = os.environ.get("DRIVER_PATH", "chromedriver")


@pytest.fixture(scope="session")
def session():
    session = webdriver.Chrome(driver_path)
    time.sleep(2)
    yield session
    session.quit()
    time.sleep(2)
