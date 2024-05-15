import pytest
from tests.vvashchu import pages


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
    products_page = pages.ProductsPage(session)
    assert products_page.get_cart_badge() == 2

    # перехід в корзину
    products_page.go_to_cart_page()

    # перевірка кількості елементів в корзині
    cart_page = pages.CartPage(session)
    assert len(cart_page.get_cart_items()) == 2

    # перехід до оформлення замовлення
    cart_page.go_to_checkout_page()

    # заповнення форми замовлення
    checkout_info_page = pages.CheckoutInfoPage(session)
    checkout_info_page.fill_order_form('Jonh', 'Adams', '001011')

    # виконання замовлення
    checkout_overview_page = pages.CheckoutOverviewPage(session)
    checkout_overview_page.finish_order()

    # перевірка, що корзина пуста
    checkout_complete_page = pages.CheckoutCompletePage(session)
    checkout_complete_page.back_to_products()
    assert products_page.get_cart_badge() == 0


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
    product_page = pages.ProductsPage(session)
    assert product_page.get_cart_badge() == 2

    # перехід в корзину
    product_page.go_to_cart_page()

    # перевірка кількості елементів в корзині
    cart_page = pages.CartPage(session)
    assert len(cart_page.get_cart_items()) == 2

    # видалення елементу
    cart_page.remove_cart_item(0)

    # перевірка кількості елементів в корзині
    assert len(cart_page.get_cart_items()) == 1


def test_checkout_disabled_if_cart_empty(session):
    """
    go to the  cart
    check if checkout is disabled
    """

    # перехід в корзину
    product_page = pages.ProductsPage(session)
    product_page.go_to_cart_page()

    # перевірка кількості елементів в корзині
    cart_page = pages.CartPage(session)
    assert len(cart_page.get_cart_items()) == 0

    cart_page = pages.CartPage(session)
    assert cart_page.is_checkout_enabled() is True
