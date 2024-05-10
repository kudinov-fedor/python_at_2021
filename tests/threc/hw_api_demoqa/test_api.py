
from tests.threc.hw_api_demoqa.api_client import ApiClient
from tests.threc.hw_api_demoqa.constants import Site
import json


def test_user_login():
    user = ApiClient(Site.USER, Site.PASSWORD)
    user_data = user.user_login()
    user_str = json.dumps(user_data)
    data = json.loads(user_str)
    assert data["username"] == Site.USER


def test_token_status():
    token = ApiClient(Site.USER, Site.PASSWORD).generate_token()
    token_str = json.dumps(token)
    data = json.loads(token_str)
    assert data["status"] == "Success"


def test_get_book():
    book = ApiClient(Site.USER, Site.PASSWORD)
    book.user_login()
    one = book.get_book().get('isbn')
    assert one == Site.ISBN_ID
