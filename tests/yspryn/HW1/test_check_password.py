import pytest
from tests.yspryn.HW1.check_password import check_password


@pytest.mark.parametrize("password, res", [
    pytest.param("Pwd123!@", True, id="length = 8"),
    pytest.param("Pwd12!@", False, id="length = 7"),
    pytest.param("Pwd1234567890!@", True, id="length = 15"),
    pytest.param("Password12345678901234567890!@#", False, id="length = 31"),
    pytest.param("Password12345678901234567890!@", True, id="length = 30")
])
def test_password_length(password, res):
    assert check_password(password) == res


@pytest.mark.parametrize("password, res", [
    pytest.param("", False, id="empty password"),
    pytest.param("          ", False, id="only empty spaces"),
    pytest.param("Qwertyasdf", False, id="only letters"),
    pytest.param("1234567890", False, id="only numbers"),
    pytest.param("!@#$%^&*()", False, id="only special character"),
    pytest.param("pwd1234567890!@", False, id="no uppercase letters"),
    pytest.param("pwd_______!@", False, id="no numbers"),
    pytest.param("pwd1234567890", False, id="no special character"),
    pytest.param("!1234567890!", False, id="no letters"),
    pytest.param("!QWERTY2024!", False, id="no lowercase letters"),
    pytest.param("!Q1234567!", False, id="only one letter"),
    pytest.param("!Q1234567Юля!", False, id="not English letters"),
])
def test_password_with_incorrect_data(password, res):
    assert check_password(password) == res


@pytest.mark.parametrize("password, res", [
    pytest.param("Qwerty12345!", True, id="only one symbol"),
    pytest.param("*(Qwerty)12345!", True, id="several symbols"),
    pytest.param("!Qwerty0!", True, id="only one number"),
    pytest.param("!010Qwerty010!", True, id="several numbers"),
    pytest.param("!Ua2024Ua!", True, id="several letters")
])
def test_correct_passwords(password, res):
    assert check_password(password) == res


@pytest.mark.parametrize("number", "1234567890")
def test_all_numbers(number):
    assert check_password("!_Qwerty_" + number) is True


@pytest.mark.parametrize("letter", "abcdefghijklmnopqrstuvwxyz")
def test_all_lower_case_letters(letter):
    assert check_password("A1234567__" + letter) is True


@pytest.mark.parametrize("letter", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
def test_all_upper_case_letters(letter):
    assert check_password("x1234567__" + letter) is True


@pytest.mark.parametrize("character", "!@#$%^&*-_+=~|/:;'\",.?")
def test_all_special_characters(character):
    assert check_password("Qwerty2024" + character) is True
