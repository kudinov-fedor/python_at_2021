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


# Test all lower letters
@pytest.mark.parametrize("lower_letter", "abcdefghijklmnopqrstuvwxyz")
def test_all_lower_case_letters(lower_letter):
    pas = f"AAA123!{lower_letter}"
    assert check_password(pas) is True


# Test all upper letters
@pytest.mark.parametrize("upper_letter", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
def test_all_upper_case_letters(upper_letter):
    pas = f"aaa{upper_letter}123!"
    assert check_password(pas) is True


# Test all numbers
@pytest.mark.parametrize("numbers", "0123456789")
def test_all_numbers(numbers):
    pas = f"aaaAAA{numbers}!"
    assert check_password(pas) is True


# Test symbols can be used
@pytest.mark.parametrize("symbols", "?@!#$%&'()*+,-./:;<=>[\]^_`{|}~")
def test_defined_symbols(symbols):
    pas = f"aaaAAA1{symbols}"
    assert check_password(pas) is True


# Test password length to 7
def test_length_7():
    assert check_password("Aaaaa1!") is False


# Test password length equal to 8
def test_length_8():
    assert check_password("Aaaaaa1!") is True


# Test password length equal to 30
def test_length_30():
    assert check_password("Super_strong_secret_password1!") is True


# Test password length equal to 31
def test_length_31():
    assert check_password("Super_strong_secret_password12!") is False


# Test password is empty
def test_empty_pwd():
    assert check_password("") is False


# Test password with spaces
def test_pwd_has_no_spaces():
    assert check_password("Empty password!") is True


# Test password with letters only
def test_pwd_letters_only():
    assert check_password("Onlyletter") is False


# Test password without numbers
def test_pwd_symbols_only():
    assert check_password("Aaaa<=>!") is False


# Test password without symbols
def test_pwd_numbers_only():
    assert check_password("Aaaa1234") is False
