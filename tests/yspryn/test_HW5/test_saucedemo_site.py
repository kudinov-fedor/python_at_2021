import pytest
from tests.yspryn.test_HW5 import pages


LOGIN_PAGE = "https://www.saucedemo.com/inventory.html"


def test_user_login(session):
    assert session.current_url == LOGIN_PAGE


def test_products_available(session):
    assert pages.CatalogPage(session).get_number_of_available_items() == 6


@pytest.mark.usefixtures("add_products_to_cart")
def test_add_products_to_cart(session):
    assert pages.CatalogPage(session).check_number_of_items_added_to_cart() == '2'


@pytest.mark.usefixtures("add_products_to_cart")
def test_remove_all_from_cart(session):
    pages.CatalogPage(session).go_to_cart()
    pages.CartPage(session).remove_item_from_cart(0)
    pages.CartPage(session).remove_item_from_cart(0)
    assert pages.CatalogPage(session).check_number_of_items_added_to_cart() == 0


@pytest.mark.usefixtures("add_products_to_cart")
def test_remove_one_item_from_cart(session):
    pages.CatalogPage(session).go_to_cart()
    pages.CartPage(session).remove_item_from_cart(0)
    assert pages.CatalogPage(session).check_number_of_items_added_to_cart() == "1"
