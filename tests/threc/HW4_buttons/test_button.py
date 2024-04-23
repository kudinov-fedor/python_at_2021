import pytest
from selenium.webdriver import ActionChains as AC
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

import costants


@pytest.fixture()
def driver():
    driver = Chrome()
    driver.get(costants.URL_BUTTONS)
    driver.maximize_window()

    driver.implicitly_wait(4)

    yield driver

    # tear down
    driver.quit()


def test_button(driver):
    btn_double = driver.find_element(By.ID, "doubleClickBtn")
    scroll_origin = ScrollOrigin.from_viewport(10, 10)
    AC(driver)\
        .scroll_from_origin(scroll_origin, 0, 200)\
        .perform()
    AC(driver).double_click(btn_double).perform()

    message = driver.find_element(By.ID, "doubleClickMessage").text
    assert message in costants.MSG_DOUBLE_CLICK

    btr_right = driver.find_element(By.ID, "rightClickBtn")
    AC(driver).context_click(btr_right).perform()

    message = driver.find_element(By.ID, "rightClickMessage").text
    assert message in costants.MSG_RIGHT_CLICK

    btn_click = driver.find_element(By.XPATH, "//button[text()='Click Me']")
    AC(driver).click(on_element=btn_click).perform()

    message = driver.find_element(By.ID, "dynamicClickMessage").text
    assert message in costants.MCG_CLICK
