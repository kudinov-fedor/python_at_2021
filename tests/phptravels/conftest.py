import pytest

from selenium_helpers.session import create_session


@pytest.fixture
def session():
    return create_session()
