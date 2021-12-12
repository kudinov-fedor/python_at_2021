import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

MAIN_PAGE = 'https://demoqa.com'


@pytest.fixture
def driver():
    driver = Chrome()
    driver.get(MAIN_PAGE)
    open_elements_tab =\
        driver.find_element(By.CSS_SELECTOR,
                            'div:nth-child(1) > div >  div.card-body > h5')
    open_elements_tab.click()
    yield driver
    driver.quit()
