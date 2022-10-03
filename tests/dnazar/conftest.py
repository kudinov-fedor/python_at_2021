import pytest
from selenium.webdriver import Chrome, ChromeOptions


@pytest.fixture
def session(tmp_path):
    options = ChromeOptions()
    prefs = {"download.default_directory": str(tmp_path)}
    options.add_experimental_option("prefs", prefs)
    session = Chrome(options=options)
    session.maximize_window()
    yield session
    session.quit()
