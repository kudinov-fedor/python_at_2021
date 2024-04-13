import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
# from selenium.common import NoSuchElementException
# from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.remote.webelement import WebElement

HOST = "https://www.saucedemo.com"
LOGIN = "standard_user"
PASSWORD = "secret_sauce"
LANDING_PG = "https://www.saucedemo.com/inventory.html"
LOGOUT_PG = "https://www.saucedemo.com/"


class AddTime(Chrome):
    def execute(self, driver_command: str, params: dict = None) -> dict:
        import time
        time.sleep(1)
        return super().execute(driver_command, params)


@pytest.fixture
def start_close_session():
    session = AddTime()
    yield session
    session.quit()


@pytest.fixture(autouse=True)
def login_to_system(start_close_session):
    start_close_session.get(HOST)

    # вхід в систему
    start_close_session.find_element(By.ID, "user-name").send_keys(LOGIN)
    start_close_session.find_element(By.ID, "password").send_keys(PASSWORD)
    start_close_session.find_element(By.ID, "login-button").click()


# перевірити лендінг пейдж урлу
def test_landing_page(start_close_session):
    current_page = start_close_session.current_url
    print(current_page)
    assert current_page == LANDING_PG


# перевірити к-сть продуктів на сторінці
def test_elements(start_close_session):
    elements = start_close_session.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
    assert len(elements) == 6


# перевірити логаут користувача
def test_logout_user(start_close_session):
    start_close_session.find_element(By.ID, "react-burger-menu-btn").click()
    start_close_session.find_element(By.XPATH, ".//*[@id='logout_sidebar_link']").click()
    current_page1 = start_close_session.current_url
    cleared_un = start_close_session.find_element(By.ID, "user-name")
    cleared_pwd = start_close_session.find_element(By.ID, "password").is_displayed()
    print(current_page1)
    assert current_page1 == LOGOUT_PG
    assert cleared_un
    assert cleared_pwd
