"""
cover with tests
fix functionality according to docstring
"""

import pytest
import string


def check_password(word):
    """
    Length 8 - 30 symbols
    At least 1 letter in upper case
    At least 1 letter in lower case
    At least 1 special character

    test cases:
    1. test min max length for password (bva + ep) : e.g. Aaaaaa1! of different length
    2. no lowercase character in password : AAAAAA1!
    3. no uppercase character in password : aaaaaa1!
    4. no special character in password : Aaaaaa11

    5. check all lowercase characters
    6. check all uppercase characters
    7. check all numbers
    8. check all special characters
    """

    has_letters = set(word).intersection("abcdefghiklmnopqrstuvwxyz")
    has_big_letters = set(word).intersection("ABCDEFGHIJKMNOPQRSTUVWXYZ")
    has_numbers = set(word).intersection("012356789")
    has_symbols = set(word).intersection("!@#$%^&*()_+?><|\":}{\\[]")

    not_short = len(word) >= 8
    not_long = len(word) < 30

    return all([has_letters,
                has_big_letters,
                has_numbers,
                has_symbols,
                not_short,
                not_long])


@pytest.mark.parametrize("password,expected", [
    pytest.param("A1!a" + "a"*3, False, id="too short (tc:1_1)"),
    pytest.param("A1!a" + "a"*4, True, id="min len (tc:1_2)"),
    pytest.param("A1!a" + "a"*11, True, id="15 chars (tc:1_3)"),
    pytest.param("A1!a" + "a"*26, True, id="max len (tc:1_4)"),
    pytest.param("A1!a" + "a"*27, False, id="too long (tc:1_5)"),
    pytest.param("AAAAAA1!", False, id="no lowercase (tc:2)"),
    pytest.param("aaaaaa1!", False, id="no uppercase (tc:3)"),
    pytest.param("Aaaaaa11", False, id="no special character (tc:4)"),
])
def test_basic_rules(password, expected):
    """test whether the minimum requirements are covered (tc1-tc4) """
    assert check_password(password) == expected


@pytest.mark.parametrize("char_set, template", [
    pytest.param(string.ascii_lowercase, "AAAAA1!", id='test each lowercase (tc:5)'),
    pytest.param(string.ascii_uppercase, "aaaaa1!", id='test each uppercase (tc:6)'),
    pytest.param(string.digits, "Aaaaaa!", id='test each number (tc:7)'),
    pytest.param(string.punctuation, "Aaaaaa1", id='test each special character (tc:8)')
])
def test_every_character(char_set, template):
    """test each uppercase, lowercase, digit and special character (tc5-tc8)"""
    failed_chars = ''
    for char in char_set:
        password = template + char
        try:
            expected = check_password(password)
            assert expected
        except AssertionError:
            failed_chars += char
    if failed_chars:
        assert False, f"Failed characters are: {failed_chars}"
