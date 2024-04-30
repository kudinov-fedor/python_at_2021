import pytest
from selenium.webdriver import Chrome
from tests.khrystynatk import pages
from tests.khrystynatk.pages.base_elements import ProductsElement, CartElement
from tests.khrystynatk.pages.constants import HOST, USERNAME, PASSWORD, LANDING_PG, LOGOUT_PG, CART_PG


@pytest.fixture
def driver():
    session = Chrome()
    session.implicitly_wait(0.5)
    yield session
    session.quit()


def test_landing_page(driver):
    """
    перевірити лендінг пейдж урлу
    """
    login_page = pages.LoginPage(driver).open_page(HOST)
    login_page.input_creds(USERNAME, PASSWORD)\
        .submit_form()
    landing_page = pages.BasePage(driver)

    assert landing_page.get_url() == LANDING_PG


def test_elements(driver):
    """
    перевірити к-сть продуктів на сторінці
    перевірити продукт лейбл
    перевірити обмеження по ціні
    """
    login_page = pages.LoginPage(driver).open_page(HOST)
    items_page = login_page.input_creds(USERNAME, PASSWORD)\
        .submit_form().find_product_rows()
    product = ProductsElement(items_page[0])

    assert len(items_page) == 6
    assert "Sauce Labs" in product.get_product_name()
    assert 0 < product.get_price() < 100


def test_logout_user(driver):
    """
    перевірити логаут користувача
    """
    login_page = pages.LoginPage(driver).open_page(HOST)
    logout = login_page.input_creds(USERNAME, PASSWORD)\
        .submit_form().logout_from_side_menu()

    assert logout.get_url() == LOGOUT_PG
    assert logout.find_username_field().is_displayed()
    assert logout.find_password_field().is_displayed()


def test_delete_from_cart(driver):
    """
    перевірити, карт бедж відповідає к-сті продуктів у корзині
    перевірити поточну урлу корзини
    """
    landing_page = pages.LoginPage(driver)
    landing_page.open_page(HOST)
    items_page = landing_page.input_creds(USERNAME, PASSWORD).submit_form()
    products = items_page.find_product_rows()
    product_1 = ProductsElement(products[0])
    product_2 = ProductsElement(products[1])
    product_3 = ProductsElement(products[2])
    product_1.add_to_cart()
    product_2.add_to_cart()
    product_3.add_to_cart()

    cart_page = items_page.go_to_cart()
    products = cart_page.find_cart_rows()
    product = CartElement(products[0])
    product.remove_cart_item()

    assert cart_page.get_url() == CART_PG
    assert cart_page.get_cart_badge() == 2
