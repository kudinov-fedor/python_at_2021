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


# assert check_password("sdfjJLsj123!@#") is True
# print("All checks passed")


# Test whether password length is valid
@pytest.mark.parametrize(["password", "expected_value"],[
    pytest.param("Pass_W1!", True, id="password length: 8"),
    pytest.param("PassWord!+PassWord0", True, id="password length: 19"),
    pytest.param("PassWord1-PassWord2-PassWord3-", True, id="password length: 30"),
    pytest.param("Pass_W1", False, id="password length: 7"),
    pytest.param("PassWord1-PassWord2-PassWord3-!", False, id="password length: 31")
])
def test_length(password, expected_value):
    assert check_password(password) == expected_value


# Test whether password has all needed characters
@pytest.mark.parametrize(["incomplete_password"],[
    pytest.param("this_is_password!?123", id="without upper case"),
    pytest.param("THIS_IS_PASSWORD?!123", id="without lower case"),
    pytest.param("This_Is_Password!?", id="without numbers"),
    pytest.param("ThisIsPassword123", id="without symbols"),
    pytest.param("", id="empty password")
])
def test_incomplete_password(incomplete_password):
    assert check_password(incomplete_password) is False


# Test whether all possible characters can be used
@pytest.mark.parametrize(["group_of_characters", "test_password"],[
    pytest.param("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcd123!", id="upper case letters"),
    pytest.param("abcdefghijklmnopqrstuvwxyz", "ABCD123!", id="lower case letters"),
    pytest.param("0123456789", "abcdABC!", id="numbers"),
    pytest.param("!“#$%&‘()*+,-./:;<=>?@[]^_`{|}\~", "ABCabc123", id="special symbols")    # due to https://owasp.org/www-community/password-special-characters
])
def test_all_characters(group_of_characters, test_password):
    errors = [value for value in group_of_characters if check_password(test_password + value) is False]
    assert len(errors) == 0, f"There is an error for {errors} character(s), which cannot be used in password, but should."


# Test that spaces in the password are allowed
# (best practices: every ASCII character, including the space character, should be used)
@pytest.mark.parametrize(["pw_with_space"],[
    pytest.param(" PassWord123", id="leading space"),
    pytest.param("PassWord123 ", id="trailing space"),
    pytest.param("Pass Word123", id="space inside")
])
def test_password_with_spaces(pw_with_space):
    assert check_password(pw_with_space) is True
