import pytest
from tests.threc.hw_password.check_password import check_password

@pytest.mark.positive
@pytest.mark.parametrize(["res"], [
    pytest.param('Qwerty8@', id='Password with 8 symbols'),
    pytest.param('Qwertyuiopasdfghjklzxcvbnm12@', id='Password with 30 symbols'),
    pytest.param('Qwertyuiopasdf12@', id='Password with symbols in between 8 and 30')
])
def test_password_positive(res):
    assert check_password(res)

@pytest.mark.negative('Password with one symbol')
@pytest.mark.parametrize(["res"], [
    pytest.param('1', id='Password with one symbol'),
    pytest.param(' ', id='Password with space'),
    pytest.param('', id='Empty password'),
    pytest.param('Q8@e', id='Password with less then 8 symbols'),
    pytest.param('qwertyuiop', id='Password with small letters'),
    pytest.param('12345678', id='Password with only numbers'),
    pytest.param('qwerty8@', id='Password without capital letter, but with nuber and special character'),
    pytest.param('qwerty88', id='Password without capital letter and special character, but with number'),
    pytest.param('qwerty@@', id='Password without capital letter and number, but with special character'),
    pytest.param('Qwerty88', id='Password without special characted, but with capital letter and number'),
    pytest.param('Qwerty@@', id='Password without number, but with capital letter and special symbol'),
    pytest.param('Qwe8@', id='Password with capital letter, special symbol, number, but less than 8 symbols'),
    pytest.param('Qwertyuiopasdfghjklzxcvbnmqw8@', id='Password with more that 30 symbols'),
    pytest.param("string with 123@", id='Password with several words')
])


def test_password_negative(res):
    assert check_password(res) is False


# Password with integer value instead of string
def test_raise_error():
    with pytest.raises(TypeError):
        assert check_password(123) is False
