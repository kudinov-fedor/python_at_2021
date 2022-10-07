import os
import pytest
import requests
from tests.msonta.demoqa import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Chrome, ChromeOptions


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
TMP_DIR = PROJECT_ROOT + os.sep + "tmp"


@pytest.fixture(scope="module")
def session():
    options = ChromeOptions()
    prefs = {"download.default_directory": os.path.abspath(TMP_DIR)}
    options.add_experimental_option("prefs", prefs)
    driver = Chrome(options=options)
    driver.maximize_window()
    yield driver
    _remove_downloaded_files()
    driver.quit()


def _remove_downloaded_files():
    files = [file for file in os.listdir(TMP_DIR) if file.endswith(".jpeg")]
    for file in files:
        os.remove(TMP_DIR + os.sep + file)


def test_download_file(session):
    session.get(config.HOST + "upload-download")

    FILE_NAME_DOWNLOAD = "sampleFile.jpeg"
    download_button = session.find_element(By.ID, "downloadButton")
    download_button.click()
    filepath = TMP_DIR + os.sep + FILE_NAME_DOWNLOAD
    wait = WebDriverWait(session, 5)
    wait.until(lambda _: os.path.isfile(filepath), message="Expected file not found: " + filepath)


def test_upload_file(session):
    session.get(config.HOST + "upload-download")
    FILE_NAME_UPLOAD = "avatar.png"
    PATH_UPLOAD = os.path.abspath(FILE_NAME_UPLOAD)
    upload_button = session.find_element(By.ID, "uploadFile")
    upload_button.send_keys(PATH_UPLOAD)

    assert FILE_NAME_UPLOAD in session.find_element(By.ID, "uploadedFilePath").text


def test_valid_link(session):
    session.get(config.HOST + "broken")
    link = session.find_element(By.CSS_SELECTOR, "a[href='http://demoqa.com']").get_attribute("href")
    r = requests.head(link)

    assert r.status_code == 301


def test_invalid_link(session):
    session.get(config.HOST + "broken")
    link = session.find_element(By.CSS_SELECTOR, "a[href='http://the-internet.herokuapp.com/status_codes/500']")\
        .get_attribute("href")
    r = requests.head(link)

    print(r.status_code)
    assert r.status_code == 500


@pytest.mark.xfail
def test_invalid_image(session):
    session.get(config.HOST + "broken")
    link = session.find_element(By.CSS_SELECTOR, "img[src='/images/Toolsqa_1.jpg']")\
        .get_attribute("src")
    r = requests.head(link)

    assert r.headers["Content-Type"] == "image/jpeg"
