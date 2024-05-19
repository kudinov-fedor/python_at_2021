import pytest
from tests.mariana_petrushanska.test_api_hw7.constansts import User
from tests.mariana_petrushanska.test_api_hw7.api_client import ApiClient


@pytest.fixture(autouse=True, scope="session")
def client():
    client = ApiClient(User.USER_NAME, User.USER_PASSWORD)
    client.token = client.generate_token()["token"]
    client.user_id = client.user_login()["userId"]
    client.user_authorized()
    yield client
