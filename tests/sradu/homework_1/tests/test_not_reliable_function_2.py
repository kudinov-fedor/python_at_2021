import pytest
from tests.sradu.homework_1.not_reliable_function_2 import not_reliable


def test_not_reliable_success(mocker):
    mocker.patch('tests.sradu.homework_1.not_reliable_function_2.random', return_value=0.5)
    result = not_reliable()
    assert result == 0.5


def test_not_reliable_failure(mocker):
    mocker.patch('tests.sradu.homework_1.not_reliable_function_2.random', return_value=0.49)
    with pytest.raises(RuntimeError, match=r"Res is less than 0.5:\s+0.49"):
        not_reliable()
