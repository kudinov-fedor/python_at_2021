import pytest


@pytest.fixture
def setup_db():
    """Setup db connection in main test fixture"""
    print("Setup DB session")
    db_connect = "DB Connection"

    yield db_connect
    print("Close DB connection")


@pytest.fixture
def session(setup_db):
    """Setup and Tear down for whole project"""
    print("Initializing of selenium session")
    print(f"We got db connection in Main Setup fixture: {setup_db}")
    my_session = "SELENIUM_SESSION"

    yield my_session
    print("fixture END!")
