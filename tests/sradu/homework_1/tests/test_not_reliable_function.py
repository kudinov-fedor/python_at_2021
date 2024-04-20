import pytest
from tests.sradu.homework_1.not_reliable_function import not_reliable


def test_not_reliable_success(mocker):
    mocker.patch('tests.sradu.homework_1.not_reliable_function.random.random', return_value=0.6)
    assert not_reliable() == 0.6


def test_not_reliable_failure(mocker):
    mocker.patch('tests.sradu.homework_1.not_reliable_function.random.random', return_value=0.4)
    with pytest.raises(RuntimeError) as exception_info:
        not_reliable()
    assert "Res is less than 0.5:  0.4" in str(exception_info.value)