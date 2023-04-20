import pytest
from selenium.webdriver.common.by import By

from magento_softwaretesting_board import config
from magento_softwaretesting_board.pageobject import page


@pytest.fixture
def login(session, user):

    main_page = page.HomePage(session).open()
    assert not main_page.user_logged_in()
    assert main_page \
        .click_login() \
        .login(user["login"], user["password"])

    # clean cart
    cart = main_page.get_cart()
    if cart.items_count() != 0:
        cart.get_cart_dialog().clean_cart().close()

    assert cart.items_count() == 0  # fail early if cleanup not successful
    yield main_page

    # logout
    main_page.open()
    if main_page.user_logged_in():
        main_page.click_logout()

    assert not main_page.user_logged_in()


@pytest.fixture
def login_add_item(login, session):
    home_page = page.HomePage(session)
    home_page.get_products()[-1].add_to_cart()
    yield


def test_login(session):

    session.get(config.HOST)

    session.find_element(By.CSS_SELECTOR, ".header.links li.authorization-link").click()
    session.find_element(By.CSS_SELECTOR, "#email").send_keys(config.LOGIN)
    session.find_element(By.CSS_SELECTOR, "#pass").send_keys(config.PASSWORD)
    session.find_element(By.CSS_SELECTOR, "#send2").click()


def test_login_pageobject(session, user):
    main_page = page.HomePage(session).open()
    assert not main_page.user_logged_in()
    assert main_page\
        .click_login()\
        .login(user["login"], user["password"])\
        .user_logged_in()

    # logout
    main_page.click_logout()
    assert not main_page.user_logged_in()


@pytest.mark.usefixtures("login")
def test_cart_empty(session):
    """
    check, that I am able to interact with cart if it is empty
    """

    cart = page.HomePage(session).get_cart()
    assert cart.items_count() == 0

    cart_dialog = cart.get_cart_dialog()
    assert cart_dialog.is_active()
    cart_dialog.close()
    assert not cart_dialog.is_active()

    cart.get_cart_dialog()
    items = cart_dialog.get_items()
    assert len(items) == 0


@pytest.mark.usefixtures("login_add_item")
def test_cart_not_empty(session):
    """
    check, that I am able to interact with cart
    if it has at least 1 item
    """
    home_page = page.HomePage(session)
    cart = home_page.get_cart()
    assert cart.items_count() == 1

    cart_dialog = cart.get_cart_dialog()
    assert cart_dialog.is_active()
    cart_dialog.close()
    assert not cart_dialog.is_active()

    cart.get_cart_dialog()
    items = cart_dialog.get_items()
    assert len(items) == 1


@pytest.mark.usefixtures("login")
def test_cart_add_item(session):
    """
    add 1 item and check its quantity
    """
    home_page = page.HomePage(session)
    home_page.get_products()[-1].add_to_cart()

    cart = home_page.get_cart()
    assert cart.items_count() == 1
    assert len(cart.get_cart_dialog().get_items()) == 1


@pytest.mark.usefixtures("login")
def test_cart_add_item_twice(session):
    """
    add same item twice and check its quantity
    """
    home_page = page.HomePage(session)

    home_page.get_products()[-1].add_to_cart()
    cart = home_page.get_cart()
    items = cart.get_cart_dialog().get_items()
    assert len(items) == 1
    assert items[0].get_quantity() == 1

    home_page.get_products()[-1].add_to_cart()
    cart = home_page.get_cart()
    items = cart.get_cart_dialog().get_items()
    assert len(items) == 1
    assert items[0].get_quantity() == 2
