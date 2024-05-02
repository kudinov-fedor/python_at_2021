import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


HOST = "https://demoqa.com/"


@pytest.fixture
def session():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    session = webdriver.Chrome(options=chrome_options)
    yield session
    session.quit()
