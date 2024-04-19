from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
import constants


def test_textbox(driver):
    scroll_origin = ScrollOrigin.from_viewport(10, 10)

    ActionChains(driver)\
        .scroll_from_origin(scroll_origin, 0, 200)\
        .perform()

    driver.find_element(By.ID, 'submit').click()

    first_name = driver.find_element(By.ID, 'name').text
    just_first_name = first_name.removeprefix('Name:')
    assert just_first_name == constants.FIRST_NAME

    user_email = driver.find_element(By.ID, 'email').text
    just_email = user_email.removeprefix('Email:')
    assert just_email in constants.USER_EMAIL

    permanent_address = driver.find_element(By.ID, 'permanentAddress').text
    just_permanent_address = permanent_address.removeprefix('Permananet Address :')
    assert just_permanent_address in constants.PERMANENT_ADDRESS
