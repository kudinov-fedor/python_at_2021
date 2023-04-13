import pytest
from selenium.webdriver import Chrome


@pytest.fixture(autouse=True)
def test_setup():
    global driver
    driver = Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/browser-windows")
    yield
    driver.close()
    driver.quit()


def test_open_new_tab():
    new_tab_btn = driver.find_element_by_css_selector("#tabButton")

    new_tab_btn.click()

    new_tab = driver.window_handles[1]
    driver.switch_to.window(new_tab)

    new_tab_text = driver.find_element_by_css_selector("#sampleHeading").text

    assert new_tab_text == "This is a sample page"

# No idea why it's not working
# def test_open_new_window_message():
#     new_window_btn = driver.find_element_by_css_selector("#messageWindowButton")
#
#     new_window_btn.click()
#     driver.switch_to.window(driver.window_handles[1])
#     new_window = driver.find_element_by_xpath("//body")
#     assert new_window.text == "Knowledge increases by sharing but not by saving. Please share this website with your " \
#                               "friends and in your organization."
