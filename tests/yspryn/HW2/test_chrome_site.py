import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


LOGIN_PAGE = "https://www.saucedemo.com/inventory.html"


# перевіряємо що юзер залогувався і відображена вірна урла
def test_user_login(session):
    assert session.current_url == LOGIN_PAGE


# перевіряємо що юзеру доступно 6 продуктів для замовлення після логіну
def test_products_available(session):
    elements = session.find_elements(By.CSS_SELECTOR, ".inventory_list .inventory_item")
    assert len(elements) == 6


# додаємо продукти до корзини і перевіряємо їх кількість після додавання
@pytest.mark.usefixtures("add_products_to_cart")
def test_add_products_to_cart(session):
    cart = session.find_element(By.ID, "shopping_cart_container")
    cart_badge = cart.find_element(By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
    assert cart_badge.text == '2'


# перевіряємо що після видалення продуктів з корзини - корзина пуста
@pytest.mark.usefixtures("add_products_to_cart", "enter_cart")
def test_remove_all_from_cart(session):
    products_in_cart = session.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
    products_in_cart[0].find_element(By.CSS_SELECTOR, ".btn_secondary.btn_small.cart_button").click()
    products_in_cart[1].find_element(By.CSS_SELECTOR, ".btn_secondary.btn_small.cart_button").click()
    cart = session.find_element(By.ID, "shopping_cart_container")
    with pytest.raises(NoSuchElementException):
        cart.find_element(By.XPATH, ".//*[contains(@class, 'shopping_cart_badge')]")
        raise AssertionError


# видалити лише 1 елемент з корзини
@pytest.mark.usefixtures("add_products_to_cart", "enter_cart")
def test_remove_one_item_from_cart(session):
    products_in_cart = session.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
    products_in_cart[0].find_element(By.CSS_SELECTOR, ".btn_secondary.btn_small.cart_button").click()
    products_in_cart = session.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
    assert len(products_in_cart) == 1
