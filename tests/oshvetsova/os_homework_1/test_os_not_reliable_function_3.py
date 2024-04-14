import pytest
from tests.oshvetsova.os_homework_1.not_reliable_function_3 import not_reliable


def test_success(mocker):
    mocker.patch('tests.oshvetsova.os_homework_1.not_reliable_function_3.random', return_value=0.9)
    res, tries = not_reliable()
    print(res, tries)
    assert res == 0.9
    assert tries == 1


def test_failure(mocker):
    mocker.patch('tests.oshvetsova.os_homework_1.not_reliable_function_3.random', return_value=0.8)
    with pytest.raises(RuntimeError, match="Its too much, total tries: 11"):
        not_reliable()
