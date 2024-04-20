import pytest
from tests.sradu.homework_1.check_password import check_password


def test_check_password_success():
    assert check_password("Psswrd1!") is True

def test_check_password_failure_not_enough_characters():
    assert check_password("Psswr1!") is False

def test_check_password_failure_no_uppercase():
    assert check_password("psswrd1!") is False

def test_check_password_failure_no_lowercase():
    assert check_password("PSSWRD1!") is False

def test_check_password_failure_no_number():
    assert check_password("Psswrdd!") is False

def test_check_password_failure_no_symbol():
    assert check_password("Psswrdd1") is False

def test_chekc_password_failure_too_many_characters():
    assert check_password("Psswrd111111111111111111111111!") is False
