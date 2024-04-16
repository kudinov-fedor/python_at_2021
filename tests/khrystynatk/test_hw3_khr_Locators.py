import pytest
from selenium.webdriver import Chrome
from selenium.common import NoSuchElementException
from tests.khrystynatk.locators import LoginPage
from tests.khrystynatk.locators import LandingPage
from tests.khrystynatk.locators import CartItems
from tests.khrystynatk.locators import SideMenu

HOST = "https://www.saucedemo.com"
LOGIN = "standard_user"
PASSWORD = "secret_sauce"
LANDING_PG = "https://www.saucedemo.com/inventory.html"
LOGOUT_PG = "https://www.saucedemo.com/"


@pytest.fixture
def driver():
    session = Chrome()
    session.implicitly_wait(0.5)
    yield session
    session.quit()


@pytest.fixture(autouse=True)
def login_to_system(driver):
    driver.get(HOST)
    driver.find_element(*LoginPage.TXT_USERNAME).send_keys(LOGIN)
    driver.find_element(*LoginPage.TXT_PASSWORD).send_keys(PASSWORD)
    driver.find_element(*LoginPage.BTN_LOGIN).click()


@pytest.fixture
@pytest.mark.usefixtures("login_to_system")
def add_to_cart(driver):
    elements = driver.find_elements(*LandingPage.LST_ITEMS)
    elements[0].find_element(*LandingPage.BTN_ADD_TO_CART).click()
    elements[1].find_element(*LandingPage.BTN_ADD_TO_CART).click()
    elements[2].find_element(*LandingPage.BTN_ADD_TO_CART).click()
    cart_link = driver.find_element(*LandingPage.LNK_CART)
    cart_link.click()


def test_landing_page(driver):
    """
    перевірити лендінг пейдж урлу
    """
    current_page = driver.current_url
    assert current_page == LANDING_PG


def test_elements(driver):
    """
    перевірити к-сть продуктів на сторінці
    """
    elements = driver.find_elements(*LandingPage.LST_ITEMS)
    assert len(elements) == 6


def test_logout_user(driver):
    """
    перевірити логаут користувача
    """
    driver.find_element(*SideMenu.BTN_BURGER_MENU).click()
    driver.find_element(*SideMenu.LNK_LOGOUT).click()
    page_url = driver.current_url
    assert page_url == LOGOUT_PG
    assert driver.find_element(*LoginPage.TXT_USERNAME).is_displayed()
    assert driver.find_element(*LoginPage.TXT_PASSWORD).is_displayed()


@pytest.mark.usefixtures("add_to_cart")
def test_delete_all_from_cart(driver):
    """
    перевірити, що сторінка корзини пуста
    перевірити поточну урлу корзини
    """
    items = driver.find_elements(*CartItems.CART_ITEMS)
    items[0].find_element(*CartItems.BTN_REMOVE_FIRST).click()
    items[1].find_element(*CartItems.BTN_REMOVE_SECOND).click()
    items[2].find_element(*CartItems.BTN_REMOVE_THIRD).click()
    cart = driver.find_element(*CartItems.CART_CONTAINER)
    with pytest.raises(NoSuchElementException):
        cart.find_element(*CartItems.IMG_CART_BADGE)
    assert driver.current_url == "https://www.saucedemo.com/cart.html"
