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


@pytest.mark.parametrize("pwd, res", [
    ("Aaaaa1!", True),                         # length<8
    ("Aaaaaa1!", True),                        # length=8
    ("Aaaaaa1!" + "a" * 22, True),             # length=30
    ("Aaaaaa1!" + "a" * 23, True),             # length>30
    ("abcdefghijklmnopqrstuvwxyz", True),      # all lower case letters can be used
    ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", True),      # all upper case letters can be used
    ("0123456789", True),                      # all numbers can be used
    ("!@#$%^&*()_+?><|\":}{\\[]", True),       # all symbols can be used
    ("Aaaaaaaa", False),                       # cannot be with letters only
    ("12345678", False),                       # cannot be with numbers only
    ("!@#$%^&*", False),                       # cannot be with symbols only
    (" ", False),                              # cannot be with space only
    (" Aa& 56 ", False),                       # cannot be with spaces
    ("", False),                               # cannot be empty
    ("с", False),                              # cannot be with not Latin letters
    ("234$%67%", False),                       # cannot be without letters
    ("Aaaa^&$#", False),                       # cannot be without numbers
    ("Aaaa1234", False)                        # cannot be without symbols
])
def test_check_pass(pwd, res):
    assert check_password(pwd) == res
