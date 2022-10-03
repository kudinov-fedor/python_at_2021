import pathlib
import os
from time import sleep
import pytest
import requests
from selenium.webdriver.common.by import By
from tests.dnazar import constants


def test_upload_download(session, tmp_path):
    FILE_NAME_UPLOAD = "upload.png"
    FILE_NAME_DOWNLOAD = "sampleFile.jpeg"
    PATH_UPLOAD = str(pathlib.Path().resolve()) + f"/test_files/{FILE_NAME_UPLOAD}"
    PATH_DOWNLOAD = f"{str(tmp_path)}/{FILE_NAME_DOWNLOAD}"
    session.get(constants.UPLOAD_DOWNLOAD_PAGE_LINK)
    upload_button = session.find_element(By.ID, "uploadFile")
    download_button = session.find_element(By.ID, "downloadButton")
    upload_button.send_keys(PATH_UPLOAD)
    assert FILE_NAME_UPLOAD in str(session.find_element(By.ID, "uploadedFilePath").text)
    download_button.click()
    for i in range(3):
        sleep(1)
        if os.path.exists(PATH_DOWNLOAD):
            break
    else:
        raise AssertionError(f"Path does not exists {PATH_DOWNLOAD}")


@pytest.mark.xfail
def test_broken_link_image(session):
    session.get(constants.BROKEN_PAGE_LINK)
    broken_link = session.find_element(By.XPATH, "//a[text()='Click Here for Broken Link']")
    broken_img = session.find_element(By.XPATH, "//p[text()='Broken image']/following-sibling::img")
    req_link = requests.head(broken_link.get_attribute("href"))
    assert 200 <= req_link.status_code < 400
    req_img = requests.head(broken_img.get_attribute("src"))
    assert req_img.headers["Content-Type"] == "image/jpeg"
