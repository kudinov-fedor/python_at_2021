import pytest


@pytest.fixture
def setup_db():
    print("I SETUP DB HERE")
    db_connect = "MY DB CONNECT"
    yield db_connect
    print("BREAK DB CONNECTION")


# setup and teardown
@pytest.fixture
def session(setup_db):
    print("INITIALIZING OF SELENIUM SESSION")
    my_session = "GREAT_SELENIUM_SESSION"
    yield my_session

    print("I WAT TO CLOSE SESSION HERE")
