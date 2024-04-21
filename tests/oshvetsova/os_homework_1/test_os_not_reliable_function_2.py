"""
Cover with tests
"""

import pytest
from tests.oshvetsova.os_homework_1.not_reliable_function_2 import not_reliable
from tests.oshvetsova.os_homework_1 import not_reliable_function_2 as module


def test_less_than_0_5(mocker):
    mocker.patch('tests.oshvetsova.os_homework_1.not_reliable_function_2.random', return_value=0.4)
    with pytest.raises(RuntimeError, match=r"Res is less than 0.5:  0.4"):
        not_reliable()


def test_equal_to_0_5(mocker):
    mocker.patch.object(module, 'random', return_value=0.5)
    assert not_reliable() == 0.5


def test_greater_to_0_5(mocker):
    mocker.patch('tests.oshvetsova.os_homework_1.not_reliable_function_2.random', return_value=0.6)
    assert not_reliable() == 0.6





