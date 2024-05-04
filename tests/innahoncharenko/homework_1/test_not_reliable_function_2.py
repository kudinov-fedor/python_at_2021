"""
Cover with tests
"""
import pytest
from random import random


def not_reliable():
    res = random()
    if res < 0.5:
        raise RuntimeError("Res is less than 0.5:  {}".format(res))
    return res


def test_equal_zero_five(mocker):
    mocker.patch(__name__ + ".random", return_value=0.5)
    assert not_reliable() == 0.5


def test_greater_zero_five(mocker):
    mocker.patch(__name__ + ".random", return_value=1)
    assert not_reliable() == 1


def test_less_zero_five(mocker):
    mocker.patch(__name__ + ".random", return_value=0.4)
    with pytest.raises(RuntimeError):
        not_reliable()


def test_equal_zero(mocker):
    mocker.patch(__name__ + ".random", return_value=0)
    with pytest.raises(RuntimeError):
        not_reliable()

