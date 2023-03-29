import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from phptravels import constants


def test_login(session: WebDriver):

    # login
    session.get(constants.cust_url)
    session.find_element(By.CSS_SELECTOR, ".form-control[type='email']").send_keys(constants.cust_login)
    session.find_element(By.CSS_SELECTOR, ".form-control[type='password']").send_keys(constants.cust_pass)
    session.find_element(By.CSS_SELECTOR, ".contact-form-action  button[type='submit']").click()
    time.sleep(5)

    # logout
    session.get("https://phptravels.net/account/logout")
