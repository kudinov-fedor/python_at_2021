import pytest
from tests.khrystynatk.hw1_khr_check_password import check_password


@pytest.mark.parametrize("pwd, res", [
    ("AAAaaa!!11", True),  # check valid pass
    ("12345678", False),  # check numbers only
    ("123_5678", False),  # check pwd has no letters
    ("TestPassword", False),  # check letters only
    ("TestP@$$word", False),  # check pwd has no numbers
    ("TestP2ssw0rd", False),  # check pwd has no symbols
    ("!@#$%^&*()", False),  # check symbols only
    ("aA!1", False),  # check pwd < 8 symbols
    ("AAAaaa!1", True),  # check pwd = 8 symbols
    ("AAAaaa!1" + "1" * 23, False),  # check pwd > 30 symbols
    ("", False),  # check empty str
    ("   A1^a   ", True)  # check spaces are counted as chars
])
def test_check_pass(pwd, res):
    assert check_password(pwd) == res


@pytest.mark.skip(reason="not implemented")
def test_pwd_is_30_chars():                           # check pwd is 30 chars long
    assert check_password("AAAaaa!1" + "1" * 22)


def test_error():
    with pytest.raises(TypeError):
        check_password(12345678)


@pytest.mark.parametrize("func", [check_password])
@pytest.mark.parametrize("pwd1, data1, res1", [
    ("AAABBB1@", "abcdefghijklmnopqrstuvwxyz", False),
    ("AAaAAA1!", "abcdefghijklmnopqrstuvwxyz", True),
    ("AAaAAA1!", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", True),
    ("aaa123$%", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", False)
])
def test_lower_upper_case(func, pwd1, data1, res1):    # check pwd has lower/uppercase letters
    passwd = pwd1
    alphabet = data1
    expected = res1
    for char in passwd:
        if char in alphabet:
            expected = res1
            break
    assert func(word=pwd1) == expected
