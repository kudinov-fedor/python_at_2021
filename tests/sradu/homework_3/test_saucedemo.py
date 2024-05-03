import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from tests.sradu.homework_3.utils import wait_for_element, wait_until_all_elements_visible
from tests.sradu.homework_3.locators import (LoginPageLocators, ProductsPageLocators, ShoppingCartLocators,
                                             CheckoutInfoLocators, CheckoutOverviewLocators)

from constants import txt_low_to_high

HOST = "https://www.saucedemo.com"
LOGIN = "standard_user"
PASSWORD = "secret_sauce"


@pytest.fixture
def session():
    driver = Chrome()
    driver.get(HOST)
    yield driver
    driver.quit()


@pytest.fixture
def login(session):
    session.find_element(*LoginPageLocators.TXT_USER_NAME).send_keys(LOGIN)
    session.find_element(*LoginPageLocators.TXT_PASSWORD).send_keys(PASSWORD)
    wait_for_element(session, *LoginPageLocators.BTN_LOGIN).click()


@pytest.mark.usefixtures("login")
def test_add_products_to_cart_and_checkout(session):
    elements = wait_until_all_elements_visible(session, *ProductsPageLocators.DIV_PRODUCT_CARD)
    assert len(elements) == 6, "Expected 6 inventory items"

    # додати перший продукт в корзину
    elements[0].find_element(*ProductsPageLocators.BTN_ADD_TO_CART).click()
    # додати третій продукт в корзину
    elements[2].find_element(*ProductsPageLocators.BTN_ADD_TO_CART).click()

    # перевірити індикатор корзини
    cart_badge = session.find_element(*ShoppingCartLocators.ICON_CART_BADGE)
    assert cart_badge.text == '2', "Expected 2 items in the cart"

    # перейти в корзину
    session.find_element(*ShoppingCartLocators.DIV_CART_CONTAINER).click()

    # перевірити кількість елементів в корзині
    items = session.find_elements(*ShoppingCartLocators.DIV_CART_ITEM)
    assert len(items) == 2, "Expected 2 items in the cart checkout"

    # перейти до оформлення замовлення
    session.find_element(*ShoppingCartLocators.BTN_CHECKOUT).click()
    session.find_element(*CheckoutInfoLocators.IP_FIRST_NAME).send_keys("Jonh")
    session.find_element(*CheckoutInfoLocators.IP_LAST_NAME).send_keys("Adams")
    session.find_element(*CheckoutInfoLocators.IP_POSTAL_CODE).send_keys("001011")
    session.find_element(*CheckoutInfoLocators.BTN_CONTINUE).click()

    # виконати замовлення
    session.find_element(*CheckoutOverviewLocators.BTN_FINISH).click()
    session.find_element(*CheckoutOverviewLocators.BTN_BACK_HOME).click()

    # перевірити, що корзина пуста
    cart = session.find_element(*ShoppingCartLocators.DIV_CART_CONTAINER)
    with pytest.raises(NoSuchElementException):
        cart.find_element(*ShoppingCartLocators.ICON_CART_BADGE)


@pytest.mark.usefixtures("login")
def test_menu_items(session):
    """ перевірити кількість і назви menu items
    1 - клікнути по burger menu button
    2 - перевірити кількість items
    3 - перевірити порядок найменувань items
    """

    # перейти у меню
    wait_for_element(session, *ProductsPageLocators.BTN_BURGER_MENU).click()

    # перевірити кількість items меню
    menu_items = wait_until_all_elements_visible(session, *ProductsPageLocators.LINK_MENU_ITEM)
    assert len(menu_items) == 4

    # перевірити порядок найменувань items меню
    expected_menu_links_texts = ["All Items", "About", "Logout", "Reset App State"]
    actual_menu_links_texts = [item.text for item in menu_items]
    assert actual_menu_links_texts == expected_menu_links_texts, f"Expected menu item texts do not match"


@pytest.mark.usefixtures("login")
def test_prices_in_ascending_order(session):
    """перевірити сортування в порядку зростанння
    1 - клікнути по dropdown сортування
    2 - клікнути Price (low to high)
    3 - перевірити, що ціни на картках з товарами йдуть у зростаючому порядку
    """

    # налаштувати сортування у порядку зростання
    wait_for_element(session,*ProductsPageLocators.SELECT_SORT_PRODUCT).click()
    wait_for_element(session, *ProductsPageLocators.option_sort(txt_low_to_high)).click()

    price_elements = wait_until_all_elements_visible(session,*ProductsPageLocators.DIV_PRODUCT_PRICE)

    # прибрати знак долара та конвернути значення цін до float
    prices_values = [float(price_element.text.replace('$', '')) for price_element in price_elements]

    # перевірити поточні ціни відсортованні в порядку зростання
    assert prices_values == sorted(prices_values), f"Prices are not in the ascending order: {prices_values}"
