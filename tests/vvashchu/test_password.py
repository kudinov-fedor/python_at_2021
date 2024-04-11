import pytest


def check_password(word):
    """
    Length 8 - 30 symbols
    At least 1 letter in upper case
    At least 1 letter in lower case
    At least 1 special character
    """

    has_letters = set(word).intersection("abcdefghijklmnopqrstuvwxyz")
    has_big_letters = set(word).intersection("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    has_numbers = set(word).intersection("0123456789")
    has_symbols = set(word).intersection("!#$%&'()*+,-./:;<=>?@][\^_`|~\":}{\\")

    not_short = len(word) >= 8
    not_long = len(word) <= 30

    return all([has_letters,
                has_big_letters,
                has_numbers,
                has_symbols,
                not_short,
                not_long])


@pytest.mark.parametrize("pwd, res", [
    ("Aaaaa1!", False),                         # <8
    ("Aaaaaa1!", True),                         # =8
    ("Aaaaaa1!" + "a" * 22, True),              # =30
    ("Aaaaaa1!" + "a" * 23, False)              # >30
])
def test_length(pwd, res):
    """
    password length
    """
    assert check_password(pwd) == res


@pytest.mark.parametrize("number", "1234567890")
def test_numbers(number):
    assert check_password("Qwerty!" + number) is True


@pytest.mark.parametrize("letter", "abcdefghijklmnopqrstuvwxyz")
def test_lower_case_letters(letter):
    assert check_password("A1234567!" + letter) is True


@pytest.mark.parametrize("letter", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
def test_upper_case_letters(letter):
    assert check_password("qwerty!1" + letter) is True


@pytest.mark.parametrize("character", "!#$%&'()*+,-./:;<=>?@][\^_`|~\":}{\\")
def test_special_characters(character):
    assert check_password("Qwerty1234" + character) is True


@pytest.mark.parametrize("pwd, res", [
    ("a34$%67%", False),                       # without upper case
    ("A34$%67%", False),                       # without lower case
    ("Aaaa^&$#", False),                       # without numbers
    ("Aaaa1234", False)                        # without symbols
])
def test_needed_characters(pwd, res):
    """
    if all needed characters are present
    """
    assert check_password(pwd) == res


@pytest.mark.parametrize("pwd, res", [
    ("", False),                               # cannot be empty
    (" ", False),                              # cannot be with space only
    ("QWd!ук1234", False)                      # cannot be with not Latin letters
])
def test_empty_space_notlatin(pwd, res):
    assert check_password(pwd) == res
