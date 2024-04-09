import pytest
from tests.khrystynatk.hw1_khr_check_password import check_password


@pytest.mark.parametrize("pwd, res", [
    ("sdfjJLsj123!@#", True),
    ("abc", False),                                         #check pwd < 8 symbols
    ("12345678", False),                                    #check numbers only
    ("123_5678", False),                                    #check numbers and symbols
    ("TestPassword", False),                                #check letters only
    ("TestP@$$word", False),                                #check letterrs and symbols
    ("TestP2ssw0rd", False),                                #check letters and numbers
    ("!@#$%^&*()", False),                                  #check symbols only
    ("sdfjJLsj123!@#sdfjJLsj123!@#sdfjJLsj123!@#", False),  #check pwd > 30 symbols
    ("sdfjJ3!@", True),                                     #check pwd = 8 symbols
    ("sdfjsj123$", False),                                  #check pwd has no UPPERCASE letters
    ("AAAA145*", False),                                    #check pwd has no LOWERCASE letters
    ("", False),                                            #check empty str
    ("   J1^p   ", True)                                    #check spaces are counted as chars
])
def test_check_pass(pwd, res):
    assert check_password(pwd) == res


@pytest.mark.parametrize("pwd1, res1", [
    ("sdfjJLsj123!@#sdfjJLsj123!@#sd", True),               #catch error for pwd = 30 symbols exactly
    ("ssdfjJLsj1.,=", True),                                #catch error for ",.=" not being considered as symbols
    ("sdfjJLsj4!", True),                                   #catch error for "4" not being considered as number
    ("jTEST5)=", True),                                     #catch error for 'j' is not listed in lowercase letters
    ("abcLLL3$", True)                                      #catch error for 'L' is not listed in uppercase letters
])
def test_error(pwd1, res1):
    with pytest.raises(AssertionError):
        assert check_password(pwd1) == res1
