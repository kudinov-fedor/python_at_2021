from random import random
import pytest
from tests.yana_pokulita import test_not_reliable_function_2_hw1

def not_reliable():
    res = random()
    if res < 0.5:
        raise RuntimeError("Res is less than 0.5:  {}".format(res))
    return res


def test_res_less_0_5(mocker):
    mocker.patch.object(test_not_reliable_function_2_hw1, 'random', return_value=0.4)
    with pytest.raises(RuntimeError):
        not_reliable()


def test_res_more_0_5(mocker):
    mocker.patch.object(test_not_reliable_function_2_hw1, 'random', return_value=0.6)
    res = not_reliable()
    assert res == 0.6


def test_res_equal_0_5(mocker):
    mocker.patch.object(test_not_reliable_function_2_hw1, 'random', return_value=0.5)
    res = not_reliable()
    assert res == 0.5


def test_res_0(mocker):
    mocker.patch.object(test_not_reliable_function_2_hw1, 'random', return_value=0)
    with pytest.raises(RuntimeError):
        not_reliable()


def test_res_1(mocker):
    mocker.patch.object(test_not_reliable_function_2_hw1, 'random', return_value=1)
    res = not_reliable()
    assert res == 1
