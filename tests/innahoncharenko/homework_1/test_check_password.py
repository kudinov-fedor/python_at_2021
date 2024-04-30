import pytest

"""
cover with tests
fix functionality according to docstring
"""

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


"""
Length 8 - 30 symbols
At least 1 letter in upper case
At least 1 letter in lower case
At least 1 special character
"""


@pytest.mark.parametrize("password", [
    "Aa+11111",
    "Aa+21111Aa+21111Aa+21111Aa+21",
])
def test_check_valid_length(password):
    assert check_password(password)


@pytest.mark.parametrize("password", [
    "Aa+1111",
    "Aa+21111Aa+21111Aa+21111Aa+2111",
    ""
])
def test_check_invalid_length(password):
    assert not check_password(password)


@pytest.mark.parametrize("password", [
    "Aa+11111",
    "Aa+21111Aa+21111Aa+21111Aa+211",
])
def test_check_valid_length(password):
    assert check_password(password)


def test_missing_number():
    assert not check_password("Aaaaaaa!")


def test_missing_uppercase():
    assert not check_password("aaaaaa1!")


def test_missing_lowercase():
    assert not check_password("AAAAAAA1!")


def test_missing_symbol():
    assert not check_password("AAAAAAA1")


@pytest.mark.parametrize("number", "0123456789")
def test_check_all_numbers(number):
    assert check_password(f"Aaaaaaa!{number}")


@pytest.mark.parametrize("uppercase_letter", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
def test_check_all_uppercase_letters(uppercase_letter):
    assert check_password(f"1aaaaaa!{uppercase_letter}")

@pytest.mark.parametrize("lowercase_letter", "abcdefghijklmnopqrstuvwxyz")
def test_check_all_lower_letters(lowercase_letter):
    assert check_password(f"1AAAAAA!{lowercase_letter}")


@pytest.mark.parametrize("letter", " !\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~")
def test_check_all_special_chars(letter):
    assert check_password(f"1AAAAAAa{letter}")