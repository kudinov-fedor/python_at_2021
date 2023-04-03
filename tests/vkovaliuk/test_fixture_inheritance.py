import pytest


@pytest.fixture(scope="class", autouse=True)
def set_up():
    """Setup and Tear down for whole project"""
    print("SetUp class")
    message = "class setup"

    yield message
    print("class END!")


def test_my_message_from_fixture(set_up):
    print(set_up)
