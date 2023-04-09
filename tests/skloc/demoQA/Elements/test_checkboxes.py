import pytest
from selenium.webdriver import Chrome


@pytest.fixture(autouse=True)
def test_setup():
    global driver
    driver = Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/checkbox")
    yield
    driver.close()
    driver.quit()

def test_mark_all_collapsed():

    top_check_btn = driver.find_element_by_css_selector(".rct-checkbox")

    top_check_btn.click()

    results = driver.find_elements_by_css_selector("#result span")

    expectedMsg = "You have selected : home desktop notes commands documents workspace react angular veu office " \
              "public private classified general downloads wordFile excelFile"

    for result in results:
        assert (expectedMsg.__contains__(result.text) and result.is_displayed())
