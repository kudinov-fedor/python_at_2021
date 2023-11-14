import string
import pytest


def check_password(word: str) -> bool:
    """
    Length 8 - 30 symbols
    At least 1 letter in upper case
    At least 1 letter in lower case
    At least 1 special character
    At least 1 number
    """
    has_letters = set(word).intersection(string.ascii_lowercase)
    has_big_letters = set(word).intersection(string.ascii_uppercase)
    has_numbers = set(word).intersection(string.digits)
    has_symbols = set(word).intersection(string.punctuation)
    has_spaces = ' ' in word
    is_right_length = 8 <= len(word) <= 30
    return all([has_letters,
                has_big_letters,
                has_numbers,
                has_symbols,
                not has_spaces,
                is_right_length])


@pytest.mark.parametrize("letter", "abcdefghijklmnopqrstuvwxyz")
def test_all_letters(letter):
    """
    test you can use all letters
    """
    val = "AAA{}123!".format(letter)
    assert check_password(val) is True


@pytest.mark.parametrize("digit", "1234567890")
def test_all_digits(digit):
    """
    test you can use all digits
    """
    val = "{}ABCdef!".format(digit)
    assert check_password(val) is True


@pytest.mark.parametrize("char", "!@#$%^&*()+-?><|:}{\[]\"\\~;'")
def test_all_chars(char):
    """
    test you can use all symbols
    """
    val = "{}ABCdef1".format(char)
    assert check_password(val) is True

    """
    test empty password
    """


def test_empty_password():
    assert check_password("") is False


def test_maximum_length():
    assert check_password("aBcDeFgH123!@#iJkLmNoPqRsTuVwX") is True


def test_minimum_length():
    assert check_password("Abc1!Def") is True


def test_valid_password_with_spaces():
    assert check_password("Abc dEf1!@#") is False
