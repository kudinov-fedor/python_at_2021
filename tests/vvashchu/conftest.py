import pytest
from selenium.webdriver import Chrome, ChromeOptions
from tests.vvashchu.pages.login_page import LoginPage
from tests.vvashchu import pages
from tests.vvashchu import constants


@pytest.fixture
def session():
    config = ChromeOptions()
    config.add_argument("--incognito")
    session = Chrome(options=config)
    yield session
    session.quit()


@pytest.fixture()
def driver():
    driver = Chrome()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def login(session):

    # вхід в систему
    LoginPage(session).open().fill_form(constants.LOGIN, constants.PASSWORD)

@pytest.fixture
@pytest.mark.usefixtures("login")
def cart_with_2_items(session):

    # products_page = pages.ProductsPage(session)
    # assert len(products_page.get_products()) == 6
    #
    # products_page.move_product_to_cart(0)
    # products_page.move_product_to_cart(3)

    elements_page = pages.ProductsPage(session)
    products = elements_page.get_products()
    assert len(products) == 6

    products[0].add_to_cart()
    products[3].add_to_cart()
