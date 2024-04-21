import pytest
from tests.sradu.homework_1.check_password import check_password

@pytest.mark.parametrize("password, expected", [
    ("Psswrd1!", True),  # Successful
    ("Psswr1!", False),  # Failure: Not enough characters
    ("psswrd1!", False), # Failure: No uppercase letters
    ("PSSWRD1!", False), # Failure: No lowercase letters
    ("Psswrdd!", False), # Failure: No number
    ("Psswrdd1", False), # Failure: No symbol
    ("Psswrd111111111111111111111111!", False)  # Failure: Too many characters
], ids=[
    "success_valid_password",
    "failure_not_enough_characters",
    "failure_no_uppercase",
    "failure_no_lowercase",
    "failure_no_number",
    "failure_no_symbol",
    "failure_too_many_characters"
])
def test_check_password(password, expected):
    assert check_password(password) is expected, f"Expected {expected} for password: {password}"
