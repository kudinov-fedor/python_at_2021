import pytest
import string


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


# Test for has_big_letters
@pytest.mark.parametrize("uc_letter", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
def test_upper_case_letters(uc_letter):
    password = f"pass{uc_letter}123!"
    assert check_password(password), f"Password check failed for {password}"


# Test for has_letters
@pytest.mark.parametrize("low_letter", "abcdefghijklmnopqrstuvwxyz")
def test_low_case_letters(low_letter):
    password = f"PASS{low_letter}123!"
    assert check_password(password), f"Password check failed for {password}"

# Test for numbers
@pytest.mark.parametrize("numeric", "0123456789")
def test_numbers(numeric):
    password = f"PassWord{numeric}!"
    assert check_password(password), f"Password check failed for {password}"


@pytest.mark.parametrize("special_characters", string.punctuation)
def test_special_characters(special_characters):
    password = f"PassWord123{special_characters}"
    assert check_password(password), f"Password check failed for {password}"


# Test for min and max character number
@pytest.mark.parametrize(["password", "expected_length"],[
    pytest.param("Pass12!", False, id="length: 7"),
    pytest.param("Pass123!", True, id="length: 8"),
    pytest.param("Password_for_Super_Admin1234!@", True, id="length: 30"),
    pytest.param("Password_for_Super_Admin12345!@", False, id="length: 31")
])
def test_length(password, expected_length):
    assert check_password(password) == expected_length
