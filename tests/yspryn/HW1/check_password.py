"""
cover with tests
fix functionality according to docstring
"""


def check_password(word):
    """
    Length 8 - 30 symbols
    At least 1 letter in upper case
    At least 1 number
    At least 1 letter in lower case
    At least 1 special character
    """

    has_letters = set(word).intersection("abcdefghijklmnopqrstuvwxyz")
    has_big_letters = set(word).intersection("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    has_numbers = set(word).intersection("0123456789")
    has_symbols = set(word).intersection("!@#$%^&*-_+=~|/:;'\",.?")

    not_short = len(word) >= 8
    not_long = len(word) <= 30

    return all([has_letters,
                has_big_letters,
                has_numbers,
                has_symbols,
                not_short,
                not_long])


assert check_password("sdfjJLsj123!@#") is True

print("All checks passed")