import pytest

def check_password(word):
    """
    Length 8 - 30 symbols
    At least 1 letter in upper case
    At least 1 letter in lower case
    At least 1 special character
    """

    has_letters = set(word).intersection("abcdefghijklmnopqrstuvwxyz")
    has_big_letters = set(word).intersection("ABCDEFGHIJKMNOPQRSTUVWXYZ")
    has_numbers = set(word).intersection("012356789")
    has_symbols = set(word).intersection("!@#$%^&*()_+?><|\":}{\\[]")

    not_short = len(word) >= 8
    not_long = len(word) <= 30

    return all([has_letters,
                has_big_letters,
                has_numbers,
                has_symbols,
                not_short,
                not_long])


#password length
@pytest.mark.parametrize("pwd, res", [
    ("Aaaaa1!", False),                         # <8
    ("Aaaaaa1!", True),                         # =8
    ("Aaaaaa1!" + "a" * 22, True),              # =30
    ("Aaaaaa1!" + "a" * 23, False)              # >30
])
def test_length(pwd, res):
    assert check_password(pwd) == res


# if all possible characters can be used
@pytest.mark.parametrize("characters, pwd", [
    ("abcdefghijklmnopqrstuvwxyz", "QWER123!"),      # all lower case letters
    ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "qwer123!"),      # all upper case letters
    ("0123456789", "qwerQWE!"),                      # all numbers
    ("!@#$%^&*()_+?><|\":}{\\[]", "QWEqwe1")         # all symbols
])
def test_all_characters(characters, pwd):
    assert check_password(characters+pwd) is False


# if all needed characters are present
@pytest.mark.parametrize("pwd, res", [
    ("a34$%67%", False),                       # without upper case
    ("A34$%67%", False),                       # without lower case
    ("Aaaa^&$#", False),                       # without numbers
    ("Aaaa1234", False)                        # without symbols
])
def test_needed_characters(pwd, res):
    assert check_password(pwd) == res


@pytest.mark.parametrize("pwd, res", [
    ("", False),                               # cannot be empty
    (" ", False),                              # cannot be with space only
    ("QWук1234", False)                        # cannot be with not Latin letters
])
def test_empty_space_notLatin(pwd, res):
    assert check_password(pwd) == res



