from tests.akaiafiuk.automation_practice.pages import MainPage


def test_items(session):
    """Verify that there is more than one item on the Main page"""
    items = MainPage(session).open().items
    assert len(items) > 1


def test_item_name(session):
    """Verify that Item Name on the Main page matches with the item name on Item page"""
    main_page = MainPage(session)
    item = main_page.open().items[0]
    item_name_main_page = item.text
    item_name_item_page = item.open_item().name
    assert item_name_main_page == item_name_item_page


def test_item_description(session):
    """Verify that Item Description is present on the Item page"""
    main_page = MainPage(session)
    item_description = main_page.open().items[0].open_item().description
    assert len(item_description) > 0


def test_open_item_using_button(session):
    """Verify that Item screen is opened after highlight an item and press More button"""
    main_page = MainPage(session)
    item = main_page.open().on_load().items[0]
    item_name_main_page = item.text
    item_name_item_page = item.click_more_button().name
    assert item_name_main_page == item_name_item_page


def test_item_form_item_name(session):
    """Verify that Item Modal is displayed and the name of the item is correct"""
    main_page = MainPage(session)
    item = main_page.open().items[0]
    item_name_main_page = item.text
    with item.open_item_info() as item_info:
        item_name_item_modal = item_info.name
    assert item_name_main_page == item_name_item_modal


def test_close_item_info_form(session):
    main_page = MainPage(session).on_load()
    item = main_page.open().items[0]
    with item.open_item_info() as item_info:
        assert isinstance(item_info.name, str)
    assert len(main_page.on_load().items) > 0
