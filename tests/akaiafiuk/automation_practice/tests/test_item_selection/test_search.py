from tests.akaiafiuk.automation_practice.pages import MainPage


def test_search_text(session):
    """Verify that search text is present on the Search Results page"""
    main_page = MainPage(session).open()
    search_text = main_page.items[0].text
    search_page = main_page.do_search(search_text).on_load()
    assert search_text.lower() in search_page.search_text.lower()


def test_search_results(session):
    """Verify that search text is present in the name of each item from search results"""
    main_page = MainPage(session).open()
    search_text = main_page.items[0].text
    search_page = main_page.do_search(search_text).on_load()
    for item in search_page.items:
        assert search_text in item.text
