
import pytest
from tests.ysemenov.hw1.not_reliable_function_3 import not_reliable


def test_not_reliable_equal_or_larger(mocker):
    """ return value equal to or larger than 0.888 on first try """
    mocker.patch('tests.ysemenov.hw1.not_reliable_function_3.random', side_effect=[0.888] + [0.887] * 10)

    assert not_reliable() == (0.888, 1)

    """ return value equal to or larger than 0.888 on last try """
    mocker.patch('tests.ysemenov.hw1.not_reliable_function_3.random', side_effect=[0.887] * 10 + [0.888])

    assert not_reliable() == (0.888, 11)


def test_not_reliable_tries(mocker):
    """ test over 10 tries with a value less than 0.888 """
    mocker.patch('tests.ysemenov.hw1.not_reliable_function_3.random', side_effect=[0.887] * 11)
    with pytest.raises(RuntimeError) as exc_info:
        not_reliable()

    assert "Its too much, total tries: 11" in str(exc_info.value)
