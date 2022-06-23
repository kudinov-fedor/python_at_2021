import pytest
import os
from selenium import webdriver


driver_path = os.environ.get("DRIVER_PATH", "chromedriver")


@pytest.fixture(scope="session")
def session():
    session = webdriver.Chrome(driver_path)
    yield session
    session.quit()

