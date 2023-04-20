import os

HOST = "https://magento.softwaretestingboard.com"
LOGIN = os.environ.get("USER_LOGIN", "test@some.com")
PASSWORD = os.environ.get("USER_PASSWORD", "Test123!@#")
USER_NAME = "test"

EXPLICIT_WAIT = 10
