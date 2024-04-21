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
    ("AAAaaa!1" + "1" * 22, True),  # check pwd = 30 symbols
    ("", False),  # check empty str
    ("AAA aaa 1@", True)  # check spaces are counted as chars
])
def test_check_pass(pwd, res):
    assert check_password(pwd) == res


@pytest.mark.skip(reason="check skip mark")
def test_pwd_is_30_chars():  # check skip mark
    assert check_password("AAAaaa!1" + "1" * 22)


def test_error():
    with pytest.raises(TypeError):
        check_password(12345678)


@pytest.mark.parametrize("pwd1, data1", [
    ("AAA111!@", "abcdefghijklmnopqrstuvwxyz"),
    ("aaa111!@", "ABCDEFGHIGKLMNOPQRSTUVWXYZ"),
    ("AAAaaa#!", "0123456789"),
    ("AAAaaa12", "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
])
def test_all_chars(pwd1, data1):
    for j, v in enumerate(data1):
        res1 = pwd1 + v
        assert check_password(res1)
