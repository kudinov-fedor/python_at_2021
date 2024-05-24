import pytest
from tests.mariana_petrushanska.test_api_hw7.constansts import User
from tests.mariana_petrushanska.test_api_hw7.api_client import ApiClient


@pytest.fixture
def client():
    client = ApiClient(User.USER_NAME, User.USER_PASSWORD)

    if client.user_exists():
        client.get_user_info()
        client.delete_user()
        client.create_user()

    client.get_user_info()

    yield client
