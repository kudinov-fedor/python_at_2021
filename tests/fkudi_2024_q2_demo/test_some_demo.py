import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from tests.fkudi_2024_q2_demo import page

HOST = "https://www.saucedemo.com"
LOGIN = "standard_user"
PASSORD = "secret_sauce"


@pytest.fixture
def session():
    session = Chrome()
    yield session
    session.quit()


def test_sample(session):

    login_page = page.LoginPage(session)
    catalog_page = login_page.open() \
        .fill_form(LOGIN, PASSORD) \
        .submit_form()

    products = catalog_page.get_products()
    assert len(products) == 6

    # додати продукти
    # catalog_page.product_add_to_cart(products[0])
    # catalog_page.product_add_to_cart(products[2])
    products[0].add_to_cart()
    products[2].add_to_cart()


    # перевірити індикатор корзини
    assert catalog_page.cart_indicator() == 2

    # перейти в корзину
    cart = session.find_element(By.ID, "shopping_cart_container")
    cart.click()

    # СТОРІНКА КОРЗИНА
    cart_elements = session.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
    assert len(cart_elements) == 2

    # перейти до оформлення замовлення
    session.find_element(By.ID, "checkout").click()

    # СТОРІНКА ОФОРМЛЕНЯ
    # заповнення форми замовлення
    session.find_element(By.ID, "first-name").send_keys("Jonh")
    session.find_element(By.ID, "last-name").send_keys("Adams")
    session.find_element(By.ID, "postal-code").send_keys("001011")
    session.find_element(By.ID, "continue").click()

    # СТОРІНКА ПІДТВЕРДЖЕННЯ
    # виконати замовлення
    session.find_element(By.ID, "finish").click()

    # СТОРІНКА THANK YOU
    # перевірити, що корзина пуста
    session.find_element(By.ID, "back-to-products").click()


    # СТОРІНКА КАТАЛОГ
    assert catalog_page.cart_indicator() == 0
