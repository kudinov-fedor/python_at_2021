import pytest
from tests.yspryn.test_HW6 import pages

LOGIN_PAGE = "https://www.saucedemo.com/inventory.html"


def test_user_login(session):
    """
    after login user is redirected to correct URL
    """
    assert session.current_url == LOGIN_PAGE


def test_products_available(session):
    """
    there are 6 products available to buy after login
    """
    assert len(pages.CatalogPage(session).list_of_products_to_buy()) == 6


def test_first_product(session):
    """
    1. check  first product name
    2. check first product prise
    """
    catalog_page = pages.CatalogPage(session).list_of_products_to_buy()
    assert catalog_page[0].get_product_name() == "Sauce Labs Backpack"
    assert catalog_page[0].get_price() == "$29.99"


@pytest.mark.usefixtures("add_products_to_cart")
def test_add_products_to_cart(session):
    """
    there are 2 items in cart
    """
    assert pages.CatalogPage(session).check_number_of_items_added_to_cart() == 2


@pytest.mark.usefixtures("add_products_to_cart")
def test_remove_all_from_cart(session):
    """
    cart is empty after removing all items
    """
    catalog_page = pages.CatalogPage(session)

    # there are 2 items in cart before deletion
    assert catalog_page.check_number_of_items_added_to_cart() == 2

    # removing 2 items from cart
    products = catalog_page.go_to_cart().list_of_products_in_cart()
    products[0].remove_cart_item()
    products[1].remove_cart_item()

    # cart is empty
    assert catalog_page.check_number_of_items_added_to_cart() == 0


@pytest.mark.usefixtures("add_products_to_cart")
def test_remove_one_item_from_cart(session):
    """this test case verifies that 1 item is left in cart after removing another one"""
    catalog_page = pages.CatalogPage(session)

    # verify that there are 2 items in cart before deletion
    assert catalog_page.check_number_of_items_added_to_cart() == 2

    # removing 1 item from cart
    catalog_page.go_to_cart().list_of_products_in_cart()[0].remove_cart_item()

    # only 1 item is left in cart
    assert catalog_page.check_number_of_items_added_to_cart() == 1
