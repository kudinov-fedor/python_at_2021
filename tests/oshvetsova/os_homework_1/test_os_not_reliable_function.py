import pytest


"""
Cover with tests
"""

import random


def not_reliable():
    res = random.random()
    if res < 0.5:
        raise RuntimeError("Res is less than 0.5:  {}".format(res))
    return res


def test_less_than_0_5(mocker):
    mocker.patch.object(random, "random", return_value=0.4)
    with pytest.raises(RuntimeError):
        not_reliable()


def test_more_than_0_5(mocker):
    mocker.patch.object(random, "random", return_value=0.6)
    assert not_reliable() == 0.6


def test_equals_to_0_5(mocker):
    mocker.patch.object(random, "random", return_value=0.5)
    assert not_reliable() == 0.5
