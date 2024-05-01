import pytest
from tests.yspryn.test_HW5 import pages


LOGIN_PAGE = "https://www.saucedemo.com/inventory.html"


def test_user_login(session):
    """verify that after login user is redirected to correct URL"""
    assert session.current_url == LOGIN_PAGE


def test_products_available(session):
    """make sure there are 6 products available to buy"""
    assert pages.CatalogPage(session).get_number_of_available_items() == 6


@pytest.mark.usefixtures("add_products_to_cart")
def test_add_products_to_cart(session):
    """make sure there are 2 items in cart"""
    assert pages.CatalogPage(session).check_number_of_items_added_to_cart() == 2


@pytest.mark.usefixtures("add_products_to_cart")
def test_remove_all_from_cart(session):
    """this test case verifies that cart is empty after removing all items"""
    catalog_page = pages.CatalogPage(session)
    cart_page = pages.CartPage(session)

    # verify that there are 2 items in cart before deletion
    assert catalog_page.check_number_of_items_added_to_cart() == 2

    # removing 2 items from cart
    catalog_page.go_to_cart()
    cart_page.remove_item_from_cart(0)
    cart_page.remove_item_from_cart(0)


    # verifying that cart is empty
    assert catalog_page.check_number_of_items_added_to_cart() == 0


@pytest.mark.usefixtures("add_products_to_cart")
def test_remove_one_item_from_cart(session):
    """this test case verifies that 1 item is left in cart after removing another one"""
    catalog_page = pages.CatalogPage(session)
    cart_page = pages.CartPage(session)

    # verify that there are 2 items in cart before deletion
    assert catalog_page.check_number_of_items_added_to_cart() == 2

    # removing 1 item from cart
    catalog_page.go_to_cart()
    cart_page.remove_item_from_cart(0)
    # verify that another 1 item is left in cart
    assert catalog_page.check_number_of_items_added_to_cart() == 1
