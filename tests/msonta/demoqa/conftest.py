from selenium.webdriver import Chrome, ChromeOptions, Remote
import pytest
from tests.msonta.demoqa import config


@pytest.fixture(scope="module")
def session():
    options = ChromeOptions()
    driver = Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def open_text_box_page(session: Remote):
    session.get(config.HOST + "text-box")
    yield session
    session.delete_all_cookies()


@pytest.fixture()
def open_button_page(session: Remote):
    session.get(config.HOST + "buttons")
    yield session
    session.delete_all_cookies()


@pytest.fixture()
def open_radio_button_page(session: Remote):
    session.get(config.HOST + "radio-button")
    yield session
    session.delete_all_cookies()
