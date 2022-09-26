from tests.akaiafiuk.automation_practice.pages import MainPage


def test_items(session):
    """Verify that there is more than one item on the Category page"""
    items = MainPage(session).open().header.categories[0].open_category().on_load().items
    assert len(items) > 1


def test_item_name(session):
    """Verify that Item Name on the Category page matches with the item name on Item page"""
    category_page = MainPage(session).open().header.categories[0].open_category().on_load()
    item_name_category_page = category_page.items[0].text
    item_name_item_page = category_page.items[0].open_item().name
    assert item_name_category_page == item_name_item_page
