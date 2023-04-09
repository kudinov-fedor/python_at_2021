from selenium.webdriver.common.by import By

from magento_softwaretesting_board import config
from magento_softwaretesting_board import page


def test_login(session):

    session.get(config.HOST)

    session.find_element(By.CSS_SELECTOR, ".header.links li.authorization-link").click()
    session.find_element(By.CSS_SELECTOR, "#email").send_keys(config.LOGIN)
    session.find_element(By.CSS_SELECTOR, "#pass").send_keys(config.PASSWORD)
    session.find_element(By.CSS_SELECTOR, "#send2").click()


def test_login_pageobject(session):
    main_page = page.HomePage(session).open()
    assert not main_page.user_logged_in()
    assert main_page\
        .click_login()\
        .login()\
        .user_logged_in()

    # logout
    main_page.click_logout()
    assert not main_page.user_logged_in()
