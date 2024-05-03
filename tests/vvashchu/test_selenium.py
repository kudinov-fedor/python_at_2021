import pytest
from selenium.common import NoSuchElementException
from tests.vvashchu.locators import Cart
from tests.vvashchu.locators import ProductPage


@pytest.mark.usefixtures("cart_with_2_items")
def test_basic(session):
    """
    check the cart indicator
    go to the cart
    check number of products in the cart
    go to checkout
    fill the form
    check if the cart is empty after order submission
    """

    # перевірка індикатора корзини
    cart = session.find_element(*ProductPage.cart)
    cart_badge = cart.find_element(*ProductPage.cart_badge)
    assert cart_badge.text == '2'

    # перехід в корзину
    cart.click()

    # перевірка кількості елементів в корзині
    cart_items = session.find_elements(*Cart.cart_items)
    assert len(cart_items) == 2

    # перехід до оформлення замовлення
    session.find_element(*Cart.checkout_btn).click()

    # заповнення форми замовлення
    session.find_element(*Cart.FirstName).send_keys("Lilia")
    session.find_element(*Cart.LastName).send_keys("Broks")
    session.find_element(*Cart.PostalCode).send_keys("001011")
    session.find_element(*Cart.continue_btn).click()

    # виконання замовлення
    session.find_element(*Cart.finish_btn).click()

    # перевірка, що корзина пуста
    session.find_element(*Cart.back_home_btn).click()
    cart = session.find_element(*ProductPage.cart)

    with pytest.raises(NoSuchElementException):
        cart.find_element(*ProductPage.cart_badge)


@pytest.mark.usefixtures("cart_with_2_items")
def test_product_can_be_removed(session):
    """
    check the cart indicator
    go to the cart
    check the number of products in the cart
    delete one product
    check the number of products in cart
    """

    # перевірка індикатора корзини
    cart = session.find_element(*ProductPage.cart)
    cart_badge = cart.find_element(*ProductPage.cart_badge)
    assert cart_badge.text == '2'

    # перехід в корзину
    cart.click()

    # перевірка кількості елементів в корзині
    cart_items = session.find_elements(*Cart.cart_items)
    assert len(cart_items) == 2

    # видалення елементу
    cart_items[0].find_element(*Cart.remove_first_item_btn).click()

    # перевірка кількості елементів в корзині
    cart_items = session.find_elements(*Cart.cart_items)
    assert len(cart_items) == 1


def test_checkout_disabled_if_cart_empty(session):
    """
    go to the cart
    check if checkout is disabled
    """

    # перехід в корзину
    cart = session.find_element(*ProductPage.cart)
    cart.click()

    # перевірка кількості елементів в корзині
    items = session.find_elements(*Cart.cart_items)
    assert len(items) == 0

    checkout_button = session.find_element(*Cart.checkout_btn).is_enabled()
    assert checkout_button is True
