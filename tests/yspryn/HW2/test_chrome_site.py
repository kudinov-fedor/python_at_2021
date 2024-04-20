import pytest
from tests.yspryn.HW2 import locators
from selenium.common import NoSuchElementException

LOGIN_PAGE = "https://www.saucedemo.com/inventory.html"

""" перевіряємо що юзер залогувався і відображена вірна урла """


def test_user_login(session):
    assert session.current_url == LOGIN_PAGE


""" перевіряємо що юзеру доступно 6 продуктів для замовлення після логіну """


def test_products_available(session):
    elements = session.find_elements(*locators.LandingPage.TABLE_PRODUCT_ITEMS)
    assert len(elements) == 6


""" додаємо продукти до корзини і перевіряємо їх кількість після додавання """


@pytest.mark.usefixtures("add_products_to_cart")
def test_add_products_to_cart(session):
    cart = session.find_element(*locators.LandingPage.BTN_CART_LOCATE)
    cart_badge = cart.find_element(*locators.LandingPage.TXT_CART_BADGE)
    assert cart_badge.text == '2'


""" перевіряємо що після видалення продуктів з корзини - корзина пуста """


@pytest.mark.usefixtures("add_products_to_cart")
def test_remove_all_from_cart(session):
    cart = session.find_element(*locators.LandingPage.BTN_CART_LOCATE)
    cart.click()

    products_in_cart = session.find_elements(*locators.CartPage.TABLE_ITEMS_IN_CART)
    products_in_cart[0].find_element(*locators.CartPage.BTN_REMOVE_FROM_CART).click()
    products_in_cart[1].find_element(*locators.CartPage.BTN_REMOVE_FROM_CART).click()

    cart = session.find_element(*locators.LandingPage.BTN_CART_LOCATE)
    with pytest.raises(NoSuchElementException):
        cart.find_element(*locators.LandingPage.TXT_CART_BADGE)
        raise AssertionError


""" видалити лише 1 елемент з корзини """


@pytest.mark.usefixtures("add_products_to_cart")
def test_remove_one_item_from_cart(session):
    cart = session.find_element(*locators.LandingPage.BTN_CART_LOCATE)
    cart.click()

    products_in_cart = session.find_elements(*locators.CartPage.TABLE_ITEMS_IN_CART)
    products_in_cart[0].find_element(*locators.CartPage.BTN_REMOVE_FROM_CART).click()
    products_in_cart = session.find_elements(*locators.CartPage.TABLE_ITEMS_IN_CART)
    assert len(products_in_cart) == 1
