import pytest


def check_password(word):
    """
    Length 8 - 30 symbols
    At least 1 letter in upper case
    At least 1 letter in lower case
    At least 1 special character
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


# Test all lower case letters can be used
@pytest.mark.parametrize("lower_case_letter", "abcdefghijklmnopqrstuvwxyz")
def test_all_lower_case_letters(lower_case_letter):
    val = "AAA{}123!".format(lower_case_letter)
    assert check_password(val) is True


# Test all upper case letters can be used
@pytest.mark.parametrize("upper_case_letter", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
def test_all_upper_case_letters(upper_case_letter):
    val = "aaa{}123!".format(upper_case_letter)
    assert check_password(val) is True


# Test all numbers can be used
@pytest.mark.parametrize("numbers", "0123456789")
def test_all_numbers(numbers):
    val = "aaaAAA{}!".format(numbers)
    assert check_password(val) is True


# Test symbols can be used
@pytest.mark.parametrize("symbols", "!#$%&'()*+,-./:;<=>?@][\^_`|~\":}{\\")
def test_defined_symbols(symbols):
    val = "aaaAAA1{}".format(symbols)
    assert check_password(val) is True


# Test password length equal to 8
def test_length_8():
    assert check_password("Test--1!") is True


# Test password length equal to 30
def test_length_30():
    assert check_password("Test--1!23Test--1!23Test--1!23") is True


# Test password length cannot be equal to 7
def test_length_7():
    assert check_password("Test-1!") is False


# Test password length cannot be equal to 31
def test_length_31():
    assert check_password("Test--1!23Test--1!23Test--1!23T") is False


# Test password cannot be empty
def test_empty_pwd():
    assert check_password("") is False


# Test password can be used with spaces
def test_pwd_has_no_spaces():
    assert check_password("Test1 data!") is True


# Test password cannot be used with letters only
def test_pwd_letters_only():
    assert check_password("Testdata") is False


# Test password cannot be used without numbers
def test_pwd_symbols_only():
    assert check_password("Test(-)!") is False


# Test password cannot be used without symbols
def test_pwd_numbers_only():
    assert check_password("Test1234") is False